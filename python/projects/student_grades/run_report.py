# 功能：成绩报告主程序，调用 score_reader 和 analyzer 生成中文成绩报告。
import os
import sys

# 运行时不生成 __pycache__，避免在项目目录落盘缓存文件
sys.dont_write_bytecode = True

from score_reader import read_scores
from analyzer import calculate_averages, find_top_student, get_subject_averages

# 数据文件绝对路径：基于本文件所在目录动态拼接，替换掉原先的硬编码绝对路径
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "scores.txt")


def main():
    """读取成绩并打印各学生平均分、平均分最高学生、各科全班平均分"""
    students = read_scores(DATA_FILE)

    if not students:
        print("未读取到任何学生数据，请检查文件路径和格式。")
        return

    # 每位学生的平均分
    avg_per_student = calculate_averages(students)
    print("========== 学生成绩报告 ==========\n")
    print("各学生平均分：")
    for name, avg in avg_per_student.items():
        print(f"{name}：{avg}")
    print()

    # 平均分最高的学生
    top = find_top_student(students)
    if top:
        top_avg = sum(top["scores"].values()) / len(top["scores"])
        print(f"平均分最高的学生是：{top['name']}，平均分 {top_avg:.1f} 分。")
    print()

    # 各科全班平均分
    subject_avgs = get_subject_averages(students)
    print("各科全班平均分：")
    for subject, avg in subject_avgs.items():
        print(f"{subject}：{avg}")


if __name__ == "__main__":
    main()
