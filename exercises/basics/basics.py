#此文件是用于练习Python基础的文件
#包含一些简单的练习题和代码示例。请根据需要进行修改和扩展。








# #你负责统计一个“夏令营”的报名情况。原始数据是一串格式凌乱的字符串，你需要提取信息并输出分析报告。
# #原始数据格式如下：
# raw_data = """
# 101, 张三, 篮球;
# 102, 李四, 游泳;
# 103, 王五, 篮球;
# 104, 赵六, 游泳;
# 105, 孙七, 羽毛球;
# 106, 周八, 篮球;
# 107, 吴九, 游泳;
# """
# #需求：
# #清洗与解析：将 raw_data 解析成一个列表，列表里每个元素是包含 编号、姓名、项目 的字典。
# #总人数统计：输出报名总人数。
# #项目热度分析：统计每个项目的报名人数，按人数降序排列输出。
# #查找功能：用户输入一个编号，程序输出该学生的姓名和项目。如果找不到，提示“未找到”.
# students = []
# for line in raw_data.splitlines():
#     if line.strip():
#         parts = line.strip(';').split(',')
#         student = {
#             '编号': parts[0].strip(),
#             '姓名': parts[1].strip(),
#             '项目': parts[2].strip()
#         }
#         students.append(student)
# project_dict = {}
# for student in students:
#     project = student.get('项目')
#     if project in project_dict:
#         project_dict[project] += 1
#     else:
#         project_dict[project] = 1
# project_dict_s = sorted(project_dict.items(), key=lambda x: x[1], reverse=True)
# print("这里是阳光夏令营报名信息分析报告，请查看详细信息：")
# search_id = input("请输入您要查询的选手编号：")
# found = False
# for item in students:
#     if item["编号"] == search_id:
#         print(f"编号对应的人是：{item['姓名']}\n参加的项目是：{item['项目']}")
#         found = True
#         break
#     if not found:
#         print("未找到")
# print("报名总人数：", len(students))
# print("项目热度分析：")
# for item in project_dict_s:
#     print(f"{item[0]}：{item[1]}人")
# print("报名情况如下：")
# print("-" * 20)
# for item in students:
#     print(f"编号：{item['编号']}")
#     print(f"姓名：{item['姓名']}")
#     print(f"项目：{item['项目']}")
#     print("-" * 20)

# #任务：设计一个“智能训练提醒”的核心逻辑。程序不追求界面美观，重点是规则引擎的设计。
# #背景：你给自己制定了一套复杂的训练规则，现在需要写一个程序，根据今天的身体状态自动判断应该做什么训练。
# # 今天的身体状态
# today_status = {
#     "体重变化趋势": "上升",  # 相比上周平均体重，可能是 "上升", "下降", "平稳"
#     "睡眠时长": 6,          # 单位：小时
#     "上周训练次数": 4,      # 单位：次
#     "身体是否有不适": False,
#     "今天是否已经训练": True,
#     "训练时间": 40,        # 单位：分钟
# }
# # 需求（按优先级判断）：
# # 安全第一：如果“身体是否有不适”为 True，无论其他条件如何，直接输出：“今天只做拉伸，让身体休息。”
# # 劳逸结合：如果“今天是否已经训练”为 True，并且时间已超过30分钟，则直接输出：“今天已完成训练，可以休息啦。” 
# # 状态不好：如果“睡眠时长”小于7小时，并且“体重变化趋势”为“上升”，则输出：“今晚早点睡，明天早起空腹有氧。”
# # 休息日调整：如果“上周训练次数”小于3次，则输出：“本周训练次数不足，今天需要补一个核心训练。”
# # 保底规则：如果以上条件都不满足，则输出：“今天可以进行常规训练，请开始你的表演！”
# if today_status["身体是否有不适"] == True:
#     print("今天只做拉伸，让身体休息。")
# elif today_status["今天是否已经训练"] == True and today_status["训练时间"] > 30:
#     print("今天已完成训练，可以休息啦。")
# elif today_status["睡眠时长"] < 7 and today_status["体重变化趋势"] == "上升":
#     print("今晚早点睡，明天早起空腹有氧。")
# elif today_status["上周训练次数"] < 3:
#     print("本周训练次数不足，今天需要补一个核心训练。")
# else:
#     print("今天可以进行常规训练，请开始你的表演！")
