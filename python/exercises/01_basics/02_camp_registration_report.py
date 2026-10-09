# 02_camp_registration_report.py
# 【练习题】夏令营报名情况分析报告（原 basics/basics.py 里被注释掉的练习）。
#
# 原题需求：
#   你负责统计一个"夏令营"的报名情况。原始数据是一串格式凌乱的字符串，
#   需要提取信息并输出分析报告。raw_data 格式如下：
#     101, 张三, 篮球;
#     102, 李四, 游泳;
#     ...
#   1) 清洗与解析：把 raw_data 解析成列表，每个元素是包含 编号/姓名/项目 的字典；
#   2) 总人数统计：输出报名总人数；
#   3) 项目热度分析：统计每个项目的报名人数，按人数降序排列输出；
#   4) 查找功能：用户输入一个编号，输出该学生的姓名和项目，找不到提示"未找到"。
#
# 修正说明：原注释代码把 `if not found: print("未找到")` 写在了 for 循环内部，
#   结果第一个人不匹配就会打印一次"未找到"。这里改成循环结束后统一判断，
#   并用固定的查询编号代替 input()，脚本可以直接跑完、不阻塞。
#
# 运行：python python/exercises/01_basics/02_camp_registration_report.py

RAW_DATA = """
101, 张三, 篮球;
102, 李四, 游泳;
103, 王五, 篮球;
104, 赵六, 游泳;
105, 孙七, 羽毛球;
106, 周八, 篮球;
107, 吴九, 游泳;
"""

# 用固定数据代替 input()：103 存在，999 不存在，两种分支都能看到输出。
SEARCH_IDS = ["103", "999"]


def parse_students(raw_data):
    """把凌乱的字符串解析成字典列表。"""
    students = []
    for line in raw_data.splitlines():
        if line.strip():
            parts = line.strip().strip(";").split(",")
            student = {
                "编号": parts[0].strip(),
                "姓名": parts[1].strip(),
                "项目": parts[2].strip(),
            }
            students.append(student)
    return students


def count_by_project(students):
    """统计每个项目的人数，返回按人数降序的 (项目, 人数) 列表。"""
    project_count = {}
    for student in students:
        project = student["项目"]
        project_count[project] = project_count.get(project, 0) + 1
    return sorted(project_count.items(), key=lambda item: item[1], reverse=True)


def find_student(students, student_id):
    """按编号查找学生，找到返回字典，找不到返回 None（修正了原来的循环内判断）。"""
    for student in students:
        if student["编号"] == student_id:
            return student
    return None


def print_report(students, search_ids):
    print("这里是阳光夏令营报名信息分析报告，请查看详细信息：")
    print(f"报名总人数：{len(students)}")

    print("\n项目热度分析（按人数降序）：")
    for project, count in count_by_project(students):
        print(f"  {project}：{count}人")

    print("\n编号查询（用固定数据代替 input()）：")
    for student_id in search_ids:
        student = find_student(students, student_id)
        if student is None:
            print(f"  查询 {student_id}：未找到")
        else:
            print(f"  查询 {student_id}：编号对应的人是 {student['姓名']}，参加的项目是 {student['项目']}")

    print("\n报名情况如下：")
    print("-" * 20)
    for student in students:
        print(f"编号：{student['编号']}")
        print(f"姓名：{student['姓名']}")
        print(f"项目：{student['项目']}")
        print("-" * 20)


def main():
    students = parse_students(RAW_DATA)
    print_report(students, SEARCH_IDS)


if __name__ == "__main__":
    main()
