# 功能：健康管理助手的命令行交互入口（添加记录 / 查看历史 / 查看统计）。
import sys

# 运行时不生成 __pycache__，避免在项目目录落盘缓存文件
sys.dont_write_bytecode = True

import health_tracker as h


def view_history(records):
    """打印全部历史记录"""
    if not records:
        print("暂无记录。")
        return
    print("\n历史体重记录：")
    for i, record in enumerate(records, 1):
        print(f"  {i}. {record['date']} — {record['weight']}kg")


def view_stats():
    """打印体重统计（记录不足时给出提示）"""
    stats = h.records_stats()
    print()
    print(h.format_stats(stats))


def main():
    """主菜单循环：1 添加 2 查看历史 3 查看统计 4 退出"""
    print("健康管理助手 v1.0")
    records = h.load_records()
    print(f"当前已加载 {len(records)} 条体重记录。")

    while True:
        print("\n--- 主菜单 ---")
        print("1. 添加体重记录")
        print("2. 查看历史记录")
        print("3. 查看统计")
        print("4. 退出")
        choice = input("请选择操作（1-4）：").strip()

        if choice == "1":
            date_str = input("请输入日期（如 2026-06-25）：").strip()
            weight_text = input("请输入体重（kg）：").strip()
            try:
                weight = h.add_record(date_str, weight_text)
            except ValueError:
                print("体重必须是数字，本次未记录。")  # 非法输入不崩溃
                continue
            print(f"已记录：{date_str}，体重 {weight}kg")
            records = h.load_records()
        elif choice == "2":
            view_history(h.load_records())
        elif choice == "3":
            view_stats()
        elif choice == "4":
            print("再见！记得明天继续记录。")
            break
        else:
            print("无效输入，请重新选择。")


if __name__ == "__main__":
    main()
