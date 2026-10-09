# 学生成绩分析

## 项目简介

读取 `data/scores.txt` 中的学生成绩，统计每位学生的平均分、平均分最高的学生以及各科全班平均分，并输出中文成绩报告。

## 文件说明

| 文件 | 说明 |
| --- | --- |
| `score_reader.py` | 数据层：`read_scores()` 读取并解析成绩文件，保留异常处理 |
| `analyzer.py` | 统计层：`calculate_averages()` / `find_top_student()` / `get_subject_averages()` |
| `run_report.py` | 入口：生成并打印成绩报告 |
| `data/scores.txt` | 成绩数据，每行 `姓名,语文,数学,英语`（UTF-8） |

数据文件路径由 `os.path.dirname(os.path.abspath(__file__))` 动态拼接，可在任意工作目录运行。

## 运行命令

```bash
python python/projects/student_grades/run_report.py
```

无需输入（stdin），不会在仓库内产生新文件。

## 学到什么

- 按“读取 / 统计 / 展示”拆分模块，入口只负责串流程
- 用 `__file__` 定位数据文件，避免硬编码绝对路径
- 读取外部数据时跳过脏行并捕获异常，让程序不因数据问题崩溃
