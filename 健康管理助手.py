"""
健康管理助手 v1.0
功能：记录每日体重、查看历史记录、简单统计
数据存储在 weight_data.txt 文件中
"""

import os

# ==================== 数据文件名 ====================
DATA_FILE = "weight_data.txt"


# ==================== 加载历史数据 ====================
def load_data():
    """从文件加载体重记录，返回列表"""
    records = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) == 2:
                        date, weight = parts
                        records.append({"日期": date, "体重": float(weight)})
    return records


# ==================== 保存数据到文件 ====================
def save_data(records):
    """将体重记录保存到文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for record in records:
            f.write(f"{record['日期']},{record['体重']}\n")


# ==================== 添加记录 ====================
def add_record(records):
    """添加一条体重记录"""
    date = input("请输入日期（如 2025-06-25）：")
    weight = float(input("请输入体重（kg）："))
    records.append({"日期": date, "体重": weight})
    save_data(records)
    print(f"已记录：{date}，体重 {weight}kg")


# ==================== 查看历史 ====================
def view_history(records):
    """显示所有体重记录"""
    if not records:
        print("暂无记录。")
        return
    print("\n历史体重记录：")
    for i, record in enumerate(records, 1):
        print(f"  {i}. {record['日期']} — {record['体重']}kg")


# ==================== 查看统计 ====================
def view_stats(records):
    """显示体重变化统计"""
    if len(records) < 2:
        print("至少需要两条记录才能统计。")
        return

    weights = [r["体重"] for r in records]
    print(f"\n📊 体重统计：")
    print(f"  当前体重：{weights[-1]}kg")
    print(f"  初始体重：{weights[0]}kg")
    print(f"  总体变化：{weights[-1] - weights[0]:+.1f}kg")
    print(f"  最低体重：{min(weights)}kg")
    print(f"  最高体重：{max(weights)}kg")

    # 计算最近一周趋势（最多取最后7条）
    recent = weights[-7:]
    if len(recent) >= 2:
        trend = recent[-1] - recent[0]
        direction = "↓下降" if trend < 0 else ("↑上升" if trend > 0 else "→持平")
        print(f"  近期趋势（最近{len(recent)}次）：{direction} {trend:+.1f}kg")


# ==================== 主菜单 ====================
def main():
    records = load_data()
    print("🏃 健康管理助手 v1.0")
    print(f"当前已加载 {len(records)} 条体重记录。")

    while True:
        print("\n--- 主菜单 ---")
        print("1. 添加体重记录")
        print("2. 查看历史记录")
        print("3. 查看统计")
        print("4. 退出")
        choice = input("请选择操作（1-4）：")

        if choice == "1":
            add_record(records)
        elif choice == "2":
            view_history(records)
        elif choice == "3":
            view_stats(records)
        elif choice == "4":
            print("👋 再见！记得明天继续记录。")
            break
        else:
            print("无效输入，请重新选择。")


# ==================== 程序入口 ====================
if __name__ == "__main__":
    main()