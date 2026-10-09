#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""仓库自检脚本（三阶段）：语法编译检查 → 可运行示例逐个执行 → 模块导入检查。

用法（在仓库根目录或任意目录均可）：
    python python/tools/smoke_test.py

- 阶段一：对仓库内所有 .py 做语法编译检查（用 compile()，不落 .pyc）
- 阶段二：把「可运行清单」里的脚本用子进程逐个跑一遍，要求退出码 0
- 阶段三：把不作为脚本运行的模块 import 一次，要求不报错且没有 stdout 输出

退出码：全部通过为 0，存在失败或缺失为 1。
"""

from __future__ import annotations

import contextlib
import os
import shutil
import subprocess
import sys
import tempfile
import uuid
from pathlib import Path

# python/tools/smoke_test.py -> python/tools -> python -> 仓库根
REPO_ROOT = Path(__file__).resolve().parents[2]

# 编译检查时跳过的目录名（任意层级）
SKIP_DIRS = {".git", "__pycache__", ".dsh-scratch", ".venv", "venv", ".ruff_cache", ".pytest_cache"}

# 阶段二：需要真正执行的「可运行清单」（路径相对仓库根，统一用 / 便于跨平台）
RUNNABLE = [
    "python/exercises/01_basics/01_variables_and_flow.py",
    "python/exercises/01_basics/02_camp_registration_report.py",
    "python/exercises/01_basics/03_workout_reminder.py",
    "python/exercises/01_basics/04_data_structures.py",
    "python/exercises/02_functions/01_function_basics.py",
    "python/exercises/02_functions/02_bmi_functions.py",
    "python/exercises/03_modules_and_exceptions/01_temperature_converter.py",
    "python/exercises/03_modules_and_exceptions/02_bmi_with_exceptions.py",
    "python/exercises/03_modules_and_exceptions/03_word_counter.py",
    "python/exercises/03_modules_and_exceptions/04_mymath_package_demo.py",
    "python/exercises/04_file_io/01_file_read_write.py",
    "python/exercises/04_file_io/02_encoding_and_os.py",
    "python/exercises/05_object_oriented/01_class_basics.py",
    "python/exercises/05_object_oriented/02_encapsulation.py",
    "python/exercises/05_object_oriented/03_inheritance.py",
    "python/exercises/05_object_oriented/04_polymorphism.py",
    "python/exercises/05_object_oriented/05_static_method_rectangle.py",
    "python/exercises/05_object_oriented/06_multiple_inheritance_mro.py",
    "python/exercises/06_regex/01_re_module_basics.py",
    "python/exercises/06_regex/02_grammar_rules.py",
    "python/exercises/06_regex/03_grammar_solutions.py",
    "python/projects/student_grades/run_report.py",
    "python/projects/star_rail_battle/main.py",
    "python/projects/star_rail_battle/battle.py",
    "python/projects/star_rail_battle/skill.py",
]

TIMEOUT_SECONDS = 30
STDERR_TAIL_LINES = 15

# 阶段三在子进程里执行的导入检查脚本：先 import，再断言没有产生 stdout 输出
IMPORT_CHECK_SOURCE = """\
import importlib.util
import pathlib
import sys

target = pathlib.Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("smoke_target", target)
module = importlib.util.module_from_spec(spec)
sys.modules["smoke_target"] = module
spec.loader.exec_module(module)
sys.stdout.write("")
"""

# 兜底临时目录：仅当平台临时目录不可写时才使用（受限沙箱的常见情况）
_SCRATCH_DIR = REPO_ROOT / ".dsh-scratch"


@contextlib.contextmanager
def _temp_dir():
    """优先用标准库临时目录；不可写时回退到仓库内被忽略的 .dsh-scratch。"""
    platform_ok = True
    try:
        with tempfile.TemporaryDirectory(prefix="repo-smoke-probe-") as probe_dir:
            Path(probe_dir, "probe.txt").write_text("ok", encoding="utf-8")
    except OSError:
        platform_ok = False

    if platform_ok:
        with tempfile.TemporaryDirectory(prefix="repo-smoke-") as path:
            yield path
        return

    _SCRATCH_DIR.mkdir(parents=True, exist_ok=True)
    path = _SCRATCH_DIR / f"smoke-{os.getpid()}-{uuid.uuid4().hex[:8]}"
    path.mkdir()
    try:
        yield str(path)
    finally:
        shutil.rmtree(path, ignore_errors=True)


def configure_stdio() -> None:
    """让中文报告在 GBK 控制台也能打印：编码不变，只把无法编码的字符替换掉。

    子进程的 stderr 是用 errors="replace" 解码的，可能含 U+FFFD；
    某些 Windows 控制台（cp936）无法编码它，不兜底会导致报告本身抛 UnicodeEncodeError。
    """
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:  # pragma: no cover - 旧版/被重定向的流
            continue
        try:
            reconfigure(errors="replace")
        except (OSError, ValueError):  # pragma: no cover
            pass


def iter_py_files(root: Path):
    """递归列出仓库内所有 .py，跳过 SKIP_DIRS。"""
    for path in sorted(root.rglob("*.py")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def phase_syntax(files: list[Path]) -> list[tuple[str, str]]:
    """阶段一：语法编译检查。返回 [(文件, 错误信息)]。"""
    failures: list[tuple[str, str]] = []
    for path in files:
        rel = path.relative_to(REPO_ROOT).as_posix()
        try:
            source = path.read_bytes()
        except OSError as exc:
            failures.append((rel, f"读取失败: {exc}"))
            continue
        try:
            # 直接编译字节源码：既尊重文件内的编码声明，也不会写出 .pyc
            compile(source, str(path), "exec")
        except SyntaxError as exc:
            failures.append((rel, f"{exc.__class__.__name__}: {exc.msg} (line {exc.lineno})"))
        except ValueError as exc:
            failures.append((rel, f"{exc.__class__.__name__}: {exc}"))
    return failures


def phase_run() -> tuple[list[str], list[tuple[str, str]], list[str]]:
    """阶段二：子进程逐个运行可运行清单。

    返回 (通过列表, [(文件, 失败原因)], 缺失列表)。
    """
    passed: list[str] = []
    failed: list[tuple[str, str]] = []
    missing: list[str] = []

    for rel in RUNNABLE:
        target = REPO_ROOT / rel
        if not target.is_file():
            missing.append(rel)
            continue
        try:
            proc = subprocess.run(
                [sys.executable, str(target)],
                cwd=str(REPO_ROOT),
                stdin=subprocess.DEVNULL,
                capture_output=True,
                timeout=TIMEOUT_SECONDS,
            )
        except subprocess.TimeoutExpired:
            failed.append((rel, f"超时（>{TIMEOUT_SECONDS}s），疑似死循环或等待输入"))
            continue
        except OSError as exc:
            failed.append((rel, f"启动子进程失败: {exc}"))
            continue

        if proc.returncode == 0:
            passed.append(rel)
            continue

        stderr = proc.stderr.decode("utf-8", errors="replace").strip().splitlines()
        tail = "\n".join(stderr[-STDERR_TAIL_LINES:]) if stderr else "(无 stderr 输出)"
        stdout = proc.stdout.decode("utf-8", errors="replace").strip().splitlines()
        stdout_tail = "\n".join(stdout[-5:]) if stdout else "(无 stdout 输出)"
        failed.append(
            (
                rel,
                f"退出码 {proc.returncode}\n  --- stdout 尾部 ---\n{stdout_tail}"
                f"\n  --- stderr 尾部（最多 {STDERR_TAIL_LINES} 行）---\n{tail}",
            )
        )
    return passed, failed, missing


def phase_imports(py_files: list[Path]) -> list[tuple[str, str]]:
    """阶段三：把「不作为脚本运行」的模块单独导入一次，确认 import 时不报错。

    典型价值是 project 里的库模块（units/analyzer/health_tracker…）：
    它们不在可运行清单里，但 import 出错会让项目整体不可用。
    在一个临时目录里执行，避免 import 过程中在仓库内留下任何文件。
    """
    runnable = {rel.replace("\\", "/") for rel in RUNNABLE}
    candidates = []
    for path in py_files:
        rel = path.relative_to(REPO_ROOT).as_posix()
        if rel in runnable:
            continue
        if path.name == "__init__.py":
            continue
        candidates.append(rel)

    failures: list[tuple[str, str]] = []
    if not candidates:
        return failures

    with _temp_dir() as tmp:
        for rel in candidates:
            env = dict(os.environ)
            module_dir = (REPO_ROOT / rel).parent
            env["PYTHONPATH"] = os.pathsep.join(
                [str(REPO_ROOT), str(module_dir)]
            )
            try:
                proc = subprocess.run(
                    [sys.executable, "-c", IMPORT_CHECK_SOURCE, str(REPO_ROOT / rel)],
                    cwd=tmp,
                    stdin=subprocess.DEVNULL,
                    capture_output=True,
                    timeout=TIMEOUT_SECONDS,
                    env=env,
                )
            except subprocess.TimeoutExpired:
                failures.append((rel, f"导入超时（>{TIMEOUT_SECONDS}s）"))
                continue
            except OSError as exc:
                failures.append((rel, f"启动子进程失败: {exc}"))
                continue

            if proc.returncode != 0:
                stderr = proc.stderr.decode("utf-8", errors="replace").strip().splitlines()
                tail = "\n".join(stderr[-STDERR_TAIL_LINES:]) if stderr else "(无 stderr 输出)"
                failures.append((rel, f"import 失败（退出码 {proc.returncode}）\n{tail}"))
                continue

            output = proc.stdout.decode("utf-8", errors="replace").strip()
            if output:
                failures.append((rel, f"import 时产生了 stdout 输出：{output!r}"))
    return failures


def main() -> int:
    configure_stdio()
    print("=" * 64)
    print(f"仓库根目录：{REPO_ROOT}")
    print(f"Python：{sys.version.split()[0]}  ({sys.executable})")
    print("=" * 64)

    py_files = list(iter_py_files(REPO_ROOT))
    print(f"\n[阶段一] 语法编译检查：共 {len(py_files)} 个 .py 文件")
    syntax_failures = phase_syntax(py_files)
    if syntax_failures:
        for rel, err in syntax_failures:
            print(f"  [语法失败] {rel} -> {err}")
    else:
        print("  [OK] 所有文件语法检查通过")

    print(f"\n[阶段二] 可运行清单：共 {len(RUNNABLE)} 项（超时 {TIMEOUT_SECONDS}s，stdin=DEVNULL）")
    passed, failed, missing = phase_run()
    for rel in passed:
        print(f"  [通过] {rel}")
    for rel in missing:
        print(f"  [缺失] {rel}")
    for rel, reason in failed:
        print(f"  [失败] {rel}: {reason}")

    import_failures = phase_imports(py_files)
    print("\n[阶段三] 模块导入检查：不在可运行清单里的 .py 逐个 import（临时目录内执行）")
    if import_failures:
        for rel, reason in import_failures:
            print(f"  [失败] {rel}: {reason}")
    else:
        print("  [OK] 所有模块导入正常，且 import 时没有 stdout 输出")

    print("\n" + "=" * 64)
    print("汇总")
    print(f"  语法检查：{len(py_files) - len(syntax_failures)}/{len(py_files)} 通过")
    print(
        f"  运行清单：总数 {len(RUNNABLE)} | 通过 {len(passed)} | "
        f"失败 {len(failed)} | 缺失 {len(missing)}"
    )
    print(f"  导入检查：失败 {len(import_failures)}")
    ok = not syntax_failures and not failed and not missing and not import_failures
    print(f"  结论：{'全部通过' if ok else '未通过'}")
    print("=" * 64)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
