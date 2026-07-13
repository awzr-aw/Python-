#你负责统计一个“夏令营”的报名情况。原始数据是一串格式凌乱的字符串，你需要提取信息并输出分析报告。
#原始数据格式如下：
raw_data = """
101, 张三, 篮球;
102, 李四, 游泳;
103, 王五, 篮球;
104, 赵六, 游泳;
105, 孙七, 羽毛球;
106, 周八, 篮球;
107, 吴九, 游泳;
"""
#需求：
#清洗与解析：将 raw_data 解析成一个列表，列表里每个元素是包含 编号、姓名、项目 的字典。
#总人数统计：输出报名总人数。
#项目热度分析：统计每个项目的报名人数，按人数降序排列输出。
#查找功能：用户输入一个编号，程序输出该学生的姓名和项目。如果找不到，提示“未找到”.
students = []
for line in raw_data.splitlines():
    if line.strip():
        parts = line.strip(';').split(',')
        student = {
            '编号': parts[0].strip(),
            '姓名': parts[1].strip(),
            '项目': parts[2].strip()
        }
        students.append(student)
project_dict = {}
for student in students:
    project = student.get('项目')
    if project in project_dict:
        project_dict[project] += 1
    else:
        project_dict[project] = 1
project_dict_s = sorted(project_dict.items(), key=lambda x: x[1], reverse=True)
print("这里是阳光夏令营报名信息分析报告，请查看详细信息：")
search_id = input("请输入您要查询的选手编号：")
found = False
for item in students:
    if item["编号"] == search_id:
        print(f"编号对应的人是：{item['姓名']}\n参加的项目是：{item['项目']}")
        found = True
        break
    if not found:
        print("未找到")
print("报名总人数：", len(students))
print("项目热度分析：")
for item in project_dict_s:
    print(f"{item[0]}：{item[1]}人")
print("报名情况如下：")
print("-" * 20)
for item in students:
    print(f"编号：{item['编号']}")
    print(f"姓名：{item['姓名']}")
    print(f"项目：{item['项目']}")
    print("-" * 20)