# 健康管理助手

## 项目简介

记录每日体重、查看历史记录并做简单统计（总体变化、最低/最高体重、近期趋势），数据以文本格式保存在本地文件中。

## 文件说明

| 文件 | 说明 |
| --- | --- |
| `health_tracker.py` | 数据层 + 业务层，对外 API 见下 |
| `run.py` | 命令行交互入口（1 添加 2 查看历史 3 查看统计 4 退出） |
| `weight_data.txt` | 数据文件（`YYYY-MM-DD,66.0` 每行一条），首次运行时自动生成，不入库 |

对外 API：`DATA_FILE`（基于 `__file__` 的绝对路径）、`load_records()`、`save_records(records)`、`add_record(date_str, weight)`、`records_stats()`（不足 2 条返回 `None`）、`format_stats(stats)`、`LINE_FORMAT`；记录字段统一为 `date` / `weight`。`import health_tracker` 不会读写文件，也不会有任何 `input()`。

## 运行命令

```bash
python python/projects/health_tracker/run.py
```

需要交互输入（菜单选项、日期、体重），非法输入不会崩溃。数据文件首次运行时会写入初始记录 `2026-06-25,66.0`，此后落盘只发生在 `health_tracker/` 目录内。

## 学到什么

- 数据层与业务层分离，模块导入无副作用
- 用 `os.path.join(os.path.dirname(os.path.abspath(__file__)), ...)` 定位数据文件
- 统计逻辑返回结构化字典，格式化输出交给独立函数，便于测试
