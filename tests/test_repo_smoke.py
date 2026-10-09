#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""仓库级冒烟测试。

既可用 pytest 运行：  python -m pytest
也可用标准库运行：    python -m unittest discover -s tests -t tests

不写入被验收的项目数据：涉及 health_tracker 的用例一律把 DATA_FILE 指到临时目录。
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import os
import shutil
import sys
import tempfile
import unittest
import uuid
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SMOKE_TEST = REPO_ROOT / "python" / "tools" / "smoke_test.py"
# 兜底临时目录：仅当平台临时目录不可写（例如受限沙箱）时才使用；
# 它位于仓库内被 .gitignore 忽略的 .dsh-scratch 下，不会污染交付内容。
SCRATCH_DIR = REPO_ROOT / ".dsh-scratch"


@contextlib.contextmanager
def _fallback_temp_dir():
    """平台临时目录不可用时的兜底：在仓库 .dsh-scratch 下建目录，用完删除。"""
    SCRATCH_DIR.mkdir(parents=True, exist_ok=True)
    path = SCRATCH_DIR / f"repo-smoke-{os.getpid()}-{uuid.uuid4().hex[:8]}"
    path.mkdir()
    try:
        yield str(path)
    finally:
        shutil.rmtree(path, ignore_errors=True)


def _platform_temp_usable() -> bool:
    """探测标准库临时目录是否真的可写（有些受限环境只可建目录、不可写文件）。"""
    try:
        with tempfile.TemporaryDirectory(
            prefix="repo-smoke-probe-", ignore_cleanup_errors=True
        ) as tmp:
            probe = Path(tmp) / "probe.txt"
            probe.write_text("ok", encoding="utf-8")
            probe.unlink()
        return True
    except OSError:
        return False


@contextlib.contextmanager
def temp_data_dir():
    """给每个用例一个隔离的临时目录，避免污染仓库里的真实数据文件。

    优先使用标准库 tempfile.TemporaryDirectory（CI / 普通开发机上都可用），
    只有在平台临时目录不可写时才退回仓库内的 .dsh-scratch。
    """
    if _platform_temp_usable():
        with tempfile.TemporaryDirectory(
            prefix="repo-smoke-", ignore_cleanup_errors=True
        ) as tmp:
            yield tmp
    else:
        with _fallback_temp_dir() as tmp:
            yield tmp


def load_module_from_path(name: str, path: Path):
    """按文件路径加载模块，不修改 sys.path。"""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:  # pragma: no cover - 环境异常
        raise ImportError(f"无法加载模块: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class TestSmokeTestTool(unittest.TestCase):
    """python/tools/smoke_test.py 本身必须是可用、可编译检查通过的。"""

    def test_smoke_test_file_exists(self):
        self.assertTrue(SMOKE_TEST.is_file(), f"缺失自检脚本: {SMOKE_TEST}")

    def test_smoke_test_compiles_and_reports_no_syntax_errors(self):
        smoke = load_module_from_path("_repo_smoke_test", SMOKE_TEST)
        self.assertEqual(Path(smoke.REPO_ROOT).resolve(), REPO_ROOT.resolve())
        files = list(smoke.iter_py_files(REPO_ROOT))
        self.assertGreater(len(files), 0, "没有扫描到任何 .py 文件")
        failures = smoke.phase_syntax(files)
        self.assertEqual([], failures, f"存在语法错误: {failures}")

    def test_smoke_test_has_no_third_party_imports(self):
        source = SMOKE_TEST.read_text(encoding="utf-8")
        for banned in ("import pytest", "import requests", "import numpy"):
            self.assertNotIn(banned, source)


class TestHealthTrackerContract(unittest.TestCase):
    """health_tracker 的 API 契约（供 smoke test 与 README 引用）。"""

    HEALTH_TRACKER = REPO_ROOT / "python" / "projects" / "health_tracker" / "health_tracker.py"

    def _load(self, data_file: Path):
        self.assertTrue(
            self.HEALTH_TRACKER.is_file(),
            f"缺失 health_tracker.py: {self.HEALTH_TRACKER}",
        )
        module = load_module_from_path("_health_tracker_under_test", self.HEALTH_TRACKER)
        module.DATA_FILE = str(data_file)  # 隔离真实数据文件
        return module

    def test_required_api_is_callable(self):
        module = self._load(SCRATCH_DIR / "unused_weight_data.txt")
        for name in ("load_records", "save_records", "add_record", "records_stats", "format_stats"):
            self.assertTrue(hasattr(module, name), f"缺少 API: {name}")
            self.assertTrue(callable(getattr(module, name)), f"{name} 不可调用")
        self.assertTrue(hasattr(module, "DATA_FILE"), "缺少 DATA_FILE")

    def test_records_stats_returns_none_on_empty_data(self):
        with temp_data_dir() as tmp:
            data_file = Path(tmp) / "weight_data.txt"
            data_file.write_text("", encoding="utf-8")
            module = self._load(data_file)
            self.assertIsNone(module.records_stats())

    def test_add_record_then_stats_contract(self):
        with temp_data_dir() as tmp:
            data_file = Path(tmp) / "weight_data.txt"
            data_file.write_text("", encoding="utf-8")
            module = self._load(data_file)
            self.assertAlmostEqual(module.add_record("2026-06-25", 66.0), 66.0)
            module.add_record("2026-06-26", 65.5)
            records = module.load_records()
            self.assertEqual(2, len(records))
            self.assertEqual({"date", "weight"}, set(records[0].keys()))
            stats = module.records_stats()
            self.assertIsNotNone(stats)
            for key in ("count", "start", "current", "change", "min", "max", "trend_direction", "trend_change"):
                self.assertIn(key, stats, f"统计结果缺少键: {key}")
            text = module.format_stats(stats)
            self.assertIsInstance(text, str)
            self.assertTrue(text.strip(), "format_stats 返回空字符串")

    def test_import_has_no_side_effects(self):
        with temp_data_dir() as tmp:
            data_file = Path(tmp) / "weight_data.txt"
            module_dir = self.HEALTH_TRACKER.parent
            before = {p.name for p in module_dir.iterdir()}
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                self._load(data_file)
            after = {p.name for p in module_dir.iterdir()}
            self.assertEqual("", buf.getvalue().strip(), "import 时产生了 stdout 输出")
            self.assertEqual(before, after, "import 时在项目目录内产生了新文件")
            self.assertFalse(data_file.exists(), "import 时写入了数据文件")


class TestRepoLayout(unittest.TestCase):
    """关键路径存在性（与 task-3 的目标结构清单一致）。"""

    EXPECTED = [
        "python/exercises/01_basics/README.md",
        "python/exercises/05_object_oriented/README.md",
        "python/exercises/04_file_io/data/sample_gbk.txt",
        "python/exercises/04_file_io/data/sample_utf8.txt",
        "python/projects/student_grades/run_report.py",
        "python/projects/star_rail_battle/main.py",
        "python/projects/star_rail_battle/battle.py",
        "python/projects/star_rail_battle/skill.py",
        "python/tools/smoke_test.py",
        "python/exercises/06_regex/README.md",
        "python/exercises/06_regex/02_grammar_rules.py",
        "python/exercises/06_regex/03_grammar_solutions.py",
        "pyproject.toml",
    ]

    def test_expected_paths_exist(self):
        missing = [rel for rel in self.EXPECTED if not (REPO_ROOT / rel).is_file()]
        self.assertEqual([], missing, f"缺失文件: {missing}")

    def test_gbk_sample_bytes(self):
        path = REPO_ROOT / "python" / "exercises" / "04_file_io" / "data" / "sample_gbk.txt"
        self.assertTrue(path.is_file(), f"缺失 GBK 样例: {path}")
        self.assertEqual(
            bytes.fromhex("C4E3BAC3A3AC686C6C6F77"),
            path.read_bytes(),
            "sample_gbk.txt 字节不等于 C4 E3 BA C3 A3 AC 68 6C 6C 6F 77",
        )
        self.assertEqual("你好，hllow", path.read_bytes().decode("gbk"))
        with self.assertRaises(UnicodeDecodeError):
            path.read_bytes().decode("utf-8")


class TestRegexExercises(unittest.TestCase):
    """06_regex 的规则手册与参考答案：可导入、结果自洽。"""

    RULES = REPO_ROOT / "python" / "exercises" / "06_regex" / "02_grammar_rules.py"
    SOLUTIONS = REPO_ROOT / "python" / "exercises" / "06_regex" / "03_grammar_solutions.py"

    def test_grammar_rules_exports_phone_check(self):
        module = load_module_from_path("_grammar_rules_under_test", self.RULES)
        self.assertTrue(module.check_phone("13812345678"))
        self.assertFalse(module.check_phone("1381234567"))
        self.assertFalse(module.check_phone("23812345678"))

    def test_solutions_match_expected_results(self):
        module = load_module_from_path("_grammar_solutions_under_test", self.SOLUTIONS)
        self.assertEqual(("2026", "10", "09"), module.split_date("2026-10-09"))
        self.assertEqual({"id": "101", "name": "张三"}, module.parse_student("编号:101 姓名:张三"))
        self.assertEqual(["123", "1234"], module.find_whole_3_to_4_digits("12 123 1234 12345"))
        greedy, lazy = module.explain_greedy()
        self.assertEqual(["<b>标题</b><i>正文</i>"], greedy)
        self.assertEqual(["<b>", "</b>", "<i>", "</i>"], lazy)
        self.assertTrue(module.is_phone("13812345678"))
        self.assertFalse(module.is_phone("1381234567a"))

    def test_source_is_utf8_and_has_main_guard(self):
        for path in (self.RULES, self.SOLUTIONS):
            source = path.read_text(encoding="utf-8")  # 编码不合法会在此抛错
            self.assertIn('if __name__ == "__main__":', source, f"{path.name} 缺少入口守卫")


if __name__ == "__main__":
    unittest.main(verbosity=2)
