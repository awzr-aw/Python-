# 功能：接受学生列表，进行统计分析。
# 统计分析模块，提供平均分、最高分、各科平均分的计算函数

def calculate_averages(students):
    """返回字典：{姓名: 平均分}"""
    averages = {}
    for stu in students:
        name = stu["name"]
        scores = stu["scores"].values()
        avg = sum(scores) / len(scores) if scores else 0
        averages[name] = round(avg, 1)  # 保留一位小数
    return averages


def find_top_student(students):
    """返回平均分最高的学生信息字典"""
    if not students:
        return None
    # 按平均分从高到低排序，返回第一个
    return max(students, key=lambda s: sum(s["scores"].values()) / len(s["scores"]))


def get_subject_averages(students):
    """返回各科全班平均分字典"""
    subject_totals = {}
    subject_counts = {}
    for stu in students:
        for subject, score in stu["scores"].items():
            subject_totals[subject] = subject_totals.get(subject, 0) + score
            subject_counts[subject] = subject_counts.get(subject, 0) + 1
    subject_avgs = {}
    for subject in subject_totals:
        subject_avgs[subject] = round(subject_totals[subject] / subject_counts[subject], 1)
    return subject_avgs