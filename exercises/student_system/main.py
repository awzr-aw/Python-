# 主程序，调用 file_handler 和 analyzer 生成成绩报告
from file_handler import read_scores
from analyzer import calculate_averages, find_top_student, get_subject_averages

# 请将路径替换为你的 scores.txt 实际路径
FILE_PATH = r"C:\Users\19990\Desktop\git\exercises\student_system\scores.txt"

students = read_scores(FILE_PATH)

if not students:
    print("未读取到任何学生数据，请检查文件路径和格式。")
    exit()

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


