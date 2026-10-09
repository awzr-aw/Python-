# 02_bmi_functions.py
# 【BMI 专题】把 BMI 的多个小函数组合起来：计算、判定、拼装完整描述、体重列表分析。
# 来源：原 functions/functions.py 里的 BMI 三道题 + analyze_weights。
# 运行：python python/exercises/02_functions/02_bmi_functions.py
#
# 修正说明：
#   1) 原注释写"偏瘦、正常、偏重、肥胖"，但代码分支返回的是"超重"，注释与代码不一致，这里统一为"超重"；
#   2) 原分支区间用 18.5 / 24.9 / 29.9，会留下 24.9~25 这类空档，这里按中国成人标准改成
#      <18.5 偏瘦、18.5~23.9 正常、24.0~27.9 超重、>=28.0 肥胖；
#   3) 原来用 input() 输入身高体重，脚本自动运行会卡住，这里改用固定演示数据。


# 题目1 需求：定义一个函数 calculate_bmi(weight, height)，
# 参数是体重(kg)和身高(m)，返回 BMI 值。
def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("身高必须大于 0")
    return weight / (height ** 2)


# 题目1 需求：再写一个函数 interpret_bmi(bmi)，
# 根据 BMI 值返回体型描述（偏瘦、正常、超重、肥胖）。
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 24.0:
        return "正常"
    elif bmi < 28.0:
        return "超重"
    else:
        return "肥胖"


# 题目2 需求：定义一个函数 get_body_status(weight, height)，
# 它内部调用 calculate_bmi() 和 interpret_bmi()，
# 直接返回完整的体型描述字符串（如"你的BMI是22.5，属于正常范围"）。
def get_body_status(weight, height):
    bmi = calculate_bmi(weight, height)
    body_status = interpret_bmi(bmi)
    return f"你的BMI是{bmi:.1f}，属于{body_status}范围"


# 题目3 需求：定义一个函数 analyze_weights(weights)，
# 参数是一个体重列表，返回三个值：平均体重、最高体重、最低体重。
def analyze_weights(weights):
    if not weights:
        raise ValueError("体重列表不能为空")
    avg = sum(weights) / len(weights)
    return avg, max(weights), min(weights)


# 题目4（原文件里的嵌套函数写法）：把 interpret_bmi 定义在 get_body_status 内部，
# 演示"函数里可以再定义函数"，返回结果与题目2 相同。
def get_body_status_nested(weight, height):
    def interpret_bmi_inner(bmi):
        if bmi < 18.5:
            return "偏瘦"
        elif bmi < 24.0:
            return "正常"
        elif bmi < 28.0:
            return "超重"
        else:
            return "肥胖"

    bmi = calculate_bmi(weight, height)
    body_status = interpret_bmi_inner(bmi)
    return f"你的BMI是{bmi:.1f}，属于{body_status}范围"


def main():
    # 用固定演示数据代替 input()，脚本可以直接跑完
    weight, height = 70.0, 1.75
    print("===== 题目1：计算与判定 =====")
    bmi = calculate_bmi(weight, height)
    print(f"体重 {weight} kg，身高 {height} m -> BMI = {bmi:.2f}，体型：{interpret_bmi(bmi)}")

    print("\n===== 题目2：组合成完整描述 =====")
    print(get_body_status(weight, height))
    print(get_body_status(50.0, 1.75))
    print(get_body_status(95.0, 1.75))

    print("\n===== 题目3：体重列表分析 =====")
    weights = [70, 65, 80, 68, 72]
    avg, max_weight, min_weight = analyze_weights(weights)
    print(f"平均体重是：{avg}")
    print(f"最高体重是：{max_weight}")
    print(f"最低体重是：{min_weight}")

    print("\n===== 题目4：嵌套函数写法（效果相同）=====")
    print(get_body_status_nested(weight, height))

    print("\n===== 边界情况：身高为 0 时抛出异常 =====")
    try:
        calculate_bmi(70.0, 0)
    except ValueError as error:
        print(f"捕获到 ValueError：{error}")


if __name__ == "__main__":
    main()
