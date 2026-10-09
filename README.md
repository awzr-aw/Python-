# Python 学习仓库

> 一个计算机专业大一学生的 Python 学习路线仓库：学习笔记 + 分主题练习 + 3 个综合项目，全部零第三方依赖、开箱即跑。

## 这个仓库是什么

- **学习笔记 + 分主题练习**：`python/exercises/` 下按 6 个主题编号组织，每个主题是一组独立可运行的小脚本，覆盖基础语法 → 函数 → 模块与异常 → 文件与编码 → 面向对象 → 正则；`python/projects/` 下是 3 个把零散知识串起来的命令行项目。
- **作者背景**：计算机科学与技术专业大一学生，正在用 Python 管理自己的体态训练与减重计划，所以练习里经常出现 BMI、体重、训练计划这类题材。

## 目录结构

```text
.
├── .github/
│   └── workflows/
│       └── python-ci.yml                        # CI：3.10/3.12 矩阵跑 compileall + ruff + 自检 + pytest
├── python/
│   ├── exercises/
│   │   ├── 01_basics/
│   │   │   ├── 01_variables_and_flow.py
│   │   │   ├── 02_camp_registration_report.py
│   │   │   ├── 03_workout_reminder.py
│   │   │   ├── 04_data_structures.py
│   │   │   └── README.md
│   │   ├── 02_functions/
│   │   │   ├── 01_function_basics.py
│   │   │   └── 02_bmi_functions.py
│   │   ├── 03_modules_and_exceptions/
│   │   │   ├── data/
│   │   │   │   └── sample_text.txt
│   │   │   ├── mymath/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── advanced.py
│   │   │   │   └── basic.py
│   │   │   ├── 01_temperature_converter.py
│   │   │   ├── 02_bmi_with_exceptions.py
│   │   │   ├── 03_word_counter.py
│   │   │   ├── 04_mymath_package_demo.py
│   │   │   └── utils_temperature.py
│   │   ├── 04_file_io/
│   │   │   ├── data/
│   │   │   │   ├── sample_gbk.txt
│   │   │   │   └── sample_utf8.txt
│   │   │   ├── 01_file_read_write.py
│   │   │   └── 02_encoding_and_os.py
│   │   ├── 05_object_oriented/
│   │   │   ├── 01_class_basics.py
│   │   │   ├── 02_encapsulation.py
│   │   │   ├── 03_inheritance.py
│   │   │   ├── 04_polymorphism.py
│   │   │   ├── 05_static_method_rectangle.py
│   │   │   ├── 06_multiple_inheritance_mro.py
│   │   │   └── README.md
│   │   └── 06_regex/
│   │       ├── 01_re_module_basics.py
│   │       ├── 02_grammar_rules.py
│   │       ├── 03_grammar_solutions.py
│   │       └── README.md
│   ├── projects/
│   │   ├── health_tracker/
│   │   │   ├── health_tracker.py
│   │   │   ├── run.py
│   │   │   └── README.md
│   │   ├── star_rail_battle/
│   │   │   ├── units.py
│   │   │   ├── skill.py
│   │   │   ├── boss.py
│   │   │   ├── battle.py
│   │   │   ├── main.py
│   │   │   └── README.md
│   │   └── student_grades/
│   │       ├── data/
│   │       │   └── scores.txt
│   │       ├── analyzer.py
│   │       ├── run_report.py
│   │       ├── score_reader.py
│   │       └── README.md
│   └── tools/
│       └── smoke_test.py                        # 仓库自检脚本
├── tests/
│   ├── __init__.py
│   └── test_repo_smoke.py                       # 仓库级冒烟测试（stdlib unittest）
├── LICENSE                                      # MIT
├── pyproject.toml                               # ruff + pytest 配置
└── README.md
```

上表省略了隐藏配置文件 `.gitattributes`（统一换行、`*.txt` 关闭转换以保护样例字节）与 `.gitignore`。运行期生成的 `python/projects/health_tracker/weight_data.txt`、`__pycache__/`、`.pytest_cache/`、`.dsh-scratch/` 已被忽略，同样不在表中。

## 内容与运行命令
所有命令都以**仓库根目录**为工作目录执行；同一主题目录下的其他脚本也能用同样方式直接运行。

| 类型 | 路径 | 一句话说明 | 示例运行命令 |
| --- | --- | --- | --- |
| 练习 | [`01_basics`](python/exercises/01_basics/README.md) | 变量与流程控制、夏令营报名报告、训练提醒、列表/字典/集合 | `python python/exercises/01_basics/01_variables_and_flow.py` |
| 练习 | `02_functions` | 函数定义、参数与返回值、多返回值、BMI 计算 | `python python/exercises/02_functions/01_function_basics.py` |
| 练习 | `03_modules_and_exceptions` | 自定义模块与 `mymath` 包、`try-except-else-finally`、词频统计 | `python python/exercises/03_modules_and_exceptions/01_temperature_converter.py` |
| 练习 | `04_file_io` | 文件读写、`with` 上下文、`encoding` 与 `os.path` | `python python/exercises/04_file_io/01_file_read_write.py` |
| 练习 | [`05_object_oriented`](python/exercises/05_object_oriented/README.md) | 类与对象、封装、继承、多态、类方法/静态方法、多继承与 MRO | `python python/exercises/05_object_oriented/01_class_basics.py` |
| 练习 | [`06_regex`](python/exercises/06_regex/README.md) | `re` 模块常用函数、正则语法规则、贪婪/非贪婪与分组（含参考答案） | `python python/exercises/06_regex/01_re_module_basics.py` |
| 项目 | [student_grades](python/projects/student_grades/README.md) | 读取 `data/scores.txt`，算每人平均分、最高分学生、各科全班平均分 | `python python/projects/student_grades/run_report.py` |
| 项目 | [health_tracker](python/projects/health_tracker/README.md) | 命令行记录每日体重，查看历史并统计变化与近期趋势 | `python python/projects/health_tracker/run.py` |
| 项目 | [star_rail_battle](python/projects/star_rail_battle/README.md) | 文字版一对一回合制战斗，战技冷却 + Boss 激怒机制 | `python python/projects/star_rail_battle/main.py` |

- `student_grades` 与 `star_rail_battle` 无需任何输入，直接跑完退出；`health_tracker` 是交互式菜单（1 添加 / 2 查看历史 / 3 查看统计 / 4 退出），需要手动输入。3 个项目的入口脚本都以 `__file__` 定位自己的数据文件，因此在任何工作目录下运行结果都一致。

## 环境与运行

- **Python 3.10+**（本仓库在本机 **Python 3.14.3** 上验证通过）；**不需要任何第三方依赖**，全部使用标准库，`import` 任何模块都不会产生副作用。

```bash
# 仓库自检：语法编译检查 + 25 个可运行示例 + 模块导入检查，全通过退出码 0
python python/tools/smoke_test.py

# 运行测试（二选一）
python -m pytest                                # 需先 pip install pytest（CI 会安装）
python -m unittest discover -s tests -t tests   # 纯标准库，零依赖，效果等价
```

`smoke_test.py` 退出码 0 = 全部通过，1 = 有语法错误或运行失败；测试用例同时兼容 pytest 与标准库 unittest，本仓库不把 pytest 列为运行依赖。

## 学习进度
| 主题 | 状态 | 对应位置 |
| --- | --- | --- |
| 基础语法（变量、运算、流程控制） | ✅ | `python/exercises/01_basics/` |
| 数据类型（列表、元组、字典、集合） | ✅ | `python/exercises/01_basics/04_data_structures.py` |
| 函数（定义、参数、返回值、作用域） | ✅ | `python/exercises/02_functions/` |
| 模块与包（自定义模块、`mymath` 包） | ✅ | `python/exercises/03_modules_and_exceptions/` |
| 异常处理（try-except-else-finally） | ✅ | `python/exercises/03_modules_and_exceptions/02_bmi_with_exceptions.py` |
| 文件读写与编码（UTF-8 / GBK） | ✅ | `python/exercises/04_file_io/` |
| 面向对象（封装、继承、多态、类方法/静态方法） | ✅ | `python/exercises/05_object_oriented/` |
| 正则表达式入门（`re` 模块、字符类/量词/分组/贪婪与非贪婪/边界） | ✅ | `python/exercises/06_regex/`（含 `03_grammar_solutions.py` 参考答案） |
| 综合项目（3 个） | ✅ | `python/projects/` |
| 正则进阶（回溯与性能、`re.compile` 复用）与测试完善 | ⏳ | `tests/` 已起步 |

## 代码约定
- **目录与文件命名**：练习主题用两位数字前缀排序（`01_basics` … `06_regex`），保证文件管理器与 `glob` 的字典序一致；文件名小写下划线（如 `01_file_read_write.py`）；数据文件统一放各主题的 `data/`。
- **程序入口**：可执行脚本统一写 `if __name__ == "__main__":`，逻辑放进函数，方便被导入与测试。
- **路径处理**：数据文件路径一律基于当前文件动态拼接，绝不写死绝对路径：`os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "scores.txt")`。
- **编码约定**：源码与文本数据默认 UTF-8；`python/exercises/04_file_io/data/sample_gbk.txt` 是**故意保留的 GBK 样例**（字节 `C4 E3 BA C3 A3 AC 68 6C 6C 6F 77`，GBK 解码为「你好，hllow」，用 `utf-8` 读会抛 `UnicodeDecodeError`），专门用来练习 `encoding=` 参数与乱码排查。
- **缓存不入库**：3 个项目的脚本都设置 `sys.dont_write_bytecode = True`，运行项目不会产生 `__pycache__/`；直接跑练习脚本仍可能生成 `__pycache__/`，它与 `.pytest_cache/`、运行期生成的 `weight_data.txt` 一并由 `.gitignore` 忽略。

## 常见问题

- **Windows 下怎么运行？** cmd 可以用反斜杠：`python python\projects\student_grades\run_report.py`；PowerShell / Git Bash 用正斜杠：`python python/projects/student_grades/run_report.py`。关键是**先 cd 到仓库根目录**。
- **为什么 `health_tracker/weight_data.txt` 不进版本库？** 它是程序首次运行时自动生成的本地数据（初始记录 `2026-06-25,66.0`），会随你的体重变化而改变，属于个人数据而非源码，因此写进 `.gitignore`；删掉它再运行程序会自动重建。
- **中文乱码怎么排查？** 按顺序检查三处：① 读写文件是否给了正确的 `encoding=`（本仓库统一 UTF-8，GBK 样例除外）；② 是否误用系统默认编码（Windows 下可能是 GBK/CP936）；③ 控制台编码，cmd 可先执行 `chcp 65001`，或设置环境变量 `PYTHONUTF8=1` 后再运行。

## 仓库地址与后续计划

- 仓库：<https://github.com/awzr-aw/Python-.git>
- TODO：正则进阶（回溯与性能、`re.compile` 复用）；补齐各主题练习的单元测试，让 CI 覆盖到每个主题；再增加 1~2 个综合项目（如带数据持久化的训练计划 CLI）。
