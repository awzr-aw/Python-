# 03_workout_reminder.py
# 【练习题】"智能训练提醒"规则引擎（原 basics/basics.py 里被注释掉的练习）。
#
# 背景：你给自己制定了一套复杂的训练规则，现在需要写一个程序，
#       根据今天的身体状态自动判断应该做什么训练。
# 今天的身体状态（原注释里的示例数据）：
#   today_status = {
#       "体重变化趋势": "上升",   # 相比上周平均体重，可能是 "上升"、"下降"、"平稳"
#       "睡眠时长": 6,            # 单位：小时
#       "上周训练次数": 4,        # 单位：次
#       "身体是否有不适": False,
#       "今天是否已经训练": True,
#       "训练时间": 40,           # 单位：分钟
#   }
# 需求（按优先级从上到下判断，命中一条就返回）：
#   1) 安全第一：身体有不适 -> "今天只做拉伸，让身体休息。"
#   2) 劳逸结合：今天已训练 且 训练时间 > 30 分钟 -> "今天已完成训练，可以休息啦。"
#   3) 状态不好：睡眠 < 7 小时 且 体重趋势为"上升" -> "今晚早点睡，明天早起空腹有氧。"
#   4) 休息日调整：上周训练次数 < 3 次 -> "本周训练次数不足，今天需要补一个核心训练。"
#   5) 保底规则：以上都不满足 -> "今天可以进行常规训练，请开始你的表演！"
#
# 修正说明：原注释代码把布尔判断写成「和 True 做比较」，Python 里直接写条件本身即可；
#   这里抽成函数，方便用多组固定状态验证每一条规则。
#
# 运行：python python/exercises/01_basics/03_workout_reminder.py

# 原始状态（对应原注释里的 today_status）
BASE_STATUS = {
    "体重变化趋势": "上升",
    "睡眠时长": 6,
    "上周训练次数": 4,
    "身体是否有不适": False,
    "今天是否已经训练": True,
    "训练时间": 40,
}


def with_status(base, **changes):
    """在基础状态上覆盖若干字段，方便构造测试用例。"""
    status = dict(base)
    status.update(changes)
    return status


def decide_training(today_status):
    """规则引擎：按优先级返回今天的训练建议。"""
    if today_status["身体是否有不适"]:
        return "今天只做拉伸，让身体休息。"
    if today_status["今天是否已经训练"] and today_status["训练时间"] > 30:
        return "今天已完成训练，可以休息啦。"
    if today_status["睡眠时长"] < 7 and today_status["体重变化趋势"] == "上升":
        return "今晚早点睡，明天早起空腹有氧。"
    if today_status["上周训练次数"] < 3:
        return "本周训练次数不足，今天需要补一个核心训练。"
    return "今天可以进行常规训练，请开始你的表演！"


# (用例名, 状态)，覆盖全部 5 条规则
TEST_CASES = [
    ("原始数据（已训练 40 分钟）", BASE_STATUS),
    ("身体有不适（安全第一）", with_status(BASE_STATUS, **{"身体是否有不适": True})),
    ("未训练但睡眠不足且体重上升", with_status(BASE_STATUS, **{"今天是否已经训练": False})),
    ("睡眠充足但上周训练不足", with_status(BASE_STATUS, **{
        "睡眠时长": 8,
        "体重变化趋势": "平稳",
        "上周训练次数": 2,
        "今天是否已经训练": False,
    })),
    ("状态良好（保底规则）", with_status(BASE_STATUS, **{
        "睡眠时长": 7.5,
        "体重变化趋势": "平稳",
        "上周训练次数": 4,
        "今天是否已经训练": False,
    })),
]


def describe_status(status):
    return (
        f"不适={status['身体是否有不适']}, 已训练={status['今天是否已经训练']}, "
        f"训练时间={status['训练时间']}分钟, 睡眠={status['睡眠时长']}小时, "
        f"体重趋势={status['体重变化趋势']}, 上周训练={status['上周训练次数']}次"
    )


def main():
    print("===== 智能训练提醒：规则引擎逐条验证 =====")
    for case_name, status in TEST_CASES:
        print(f"\n[{case_name}]")
        print(f"  状态：{describe_status(status)}")
        print(f"  建议：{decide_training(status)}")


if __name__ == "__main__":
    main()
