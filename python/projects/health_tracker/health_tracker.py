# 功能：健康管理助手的数据层与业务层：读写体重记录、添加记录、统计并格式化输出。
import os

# 数据文件绝对路径：基于本文件所在目录动态拼接，保证在任何工作目录下都能定位
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "weight_data.txt")

# 每行记录的文本格式：YYYY-MM-DD,66.0（兼容原 weight_data.txt 的存储格式）
LINE_FORMAT = "{date},{weight}"

# 首次运行（数据文件不存在）时写入的初始数据，内容来自原 weight_data.txt
INITIAL_RECORDS = [{"date": "2026-06-25", "weight": 66.0}]


# ==================== 数据层 ====================
def ensure_data_file():
    """数据文件不存在时用初始数据创建，返回是否新建了文件"""
    if not os.path.exists(DATA_FILE):
        save_records(INITIAL_RECORDS)
        return True
    return False


def load_records():
    """读取全部记录，返回 [{"date": "2026-06-25", "weight": 66.0}, ...]

    首次调用时若数据文件不存在，会先写入初始数据（程序首次运行时生成，不必提交）。
    """
    ensure_data_file()
    records = []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 2:
                    continue  # 跳过格式不正确的行
                date, weight = parts[0].strip(), parts[1].strip()
                try:
                    records.append({"date": date, "weight": float(weight)})
                except ValueError:
                    continue  # 跳过体重不是数字的行
    except OSError as e:
        print(f"读取 {DATA_FILE} 失败：{e}")
    return records


def save_records(records):
    """把记录列表整体写回数据文件（覆盖写入）"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for record in records:
            f.write(LINE_FORMAT.format(date=record["date"], weight=record["weight"]) + "\n")


# ==================== 业务层 ====================
def add_record(date_str, weight):
    """追加一条体重记录并落盘，返回本次体重"""
    weight = float(weight)
    records = load_records()
    records.append({"date": date_str, "weight": weight})
    save_records(records)
    return weight


def records_stats():
    """统计体重变化：记录少于 2 条时返回 None

    返回键：count / start / current / change / min / max / trend_direction / trend_change
    """
    records = load_records()
    if len(records) < 2:
        return None

    weights = [record["weight"] for record in records]
    recent = weights[-7:]  # 近期趋势最多取最后 7 条记录
    trend_change = recent[-1] - recent[0]
    if trend_change < 0:
        direction = "↓下降"
    elif trend_change > 0:
        direction = "↑上升"
    else:
        direction = "→持平"

    return {
        "count": len(records),
        "start": weights[0],
        "current": weights[-1],
        "change": round(weights[-1] - weights[0], 1),
        "min": min(weights),
        "max": max(weights),
        "trend_direction": direction,
        "trend_change": round(trend_change, 1),
    }


def format_stats(stats):
    """把 records_stats 的结果格式化成中文多行字符串"""
    if not stats:
        return "至少需要两条记录才能统计。"
    return "\n".join([
        "体重统计：",
        f"  记录条数：{stats['count']} 条",
        f"  初始体重：{stats['start']}kg",
        f"  当前体重：{stats['current']}kg",
        f"  总体变化：{stats['change']:+.1f}kg",
        f"  最低体重：{stats['min']}kg",
        f"  最高体重：{stats['max']}kg",
        f"  近期趋势：{stats['trend_direction']} {stats['trend_change']:+.1f}kg",
    ])
