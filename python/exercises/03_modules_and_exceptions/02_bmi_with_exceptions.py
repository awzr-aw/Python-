# 02_bmi_with_exceptions.py
# 【异常处理】带异常处理的 BMI 计算器升级版。
# 来源：原 modules_and_exceptions/bmi_upgrade.py。
# 运行：python python/exercises/03_modules_and_exceptions/02_bmi_with_exceptions.py
#
# 原题需求：
#   1) 定义一个函数 input_valid_number(prompt)，反复提示用户输入数字，直到输入合法为止
#      （捕获 ValueError）；
#   2) 定义一个函数 calculate_bmi(weight, height) 计算 BMI；
#   3) 主程序调用 input_valid_number 获取体重和身高，再调用 calculate_bmi 计算并输出结果；
#   4) 如果用户输入了负数，用 raise 抛出 ValueError 并提示 "数值不能为负数"。
#
# 改动说明：原实现直接用 input()，脚本自动运行时会在第一步就阻塞等待输入。
#   这里把"输入源"换成一个固定的字符串序列（answers），判断与异常逻辑完全保留：
#   非法就继续取下一个，直到拿到合法数字。


def parse_valid_number(text):
    """把字符串转成非负浮点数；非法时抛出 ValueError。"""
    number = float(text)                 # 非数字会抛出 ValueError
    if number < 0:
        raise ValueError("数值不能为负数")   # 负数主动 raise ValueError
    return number


def input_valid_number(prompt, answers):
    """模拟"反复提示输入"：依次取 answers，直到拿到合法数字；全都不合法则返回 None。"""
    for text in answers:
        try:
            number = parse_valid_number(text)
        except ValueError as error:      # ValueError 是输入无效时抛出的异常
            print(f"{prompt}输入 {text!r} 无效：{error}")
        else:
            print(f"{prompt}采用 {text!r} -> {number}")
            return number
    print(f"{prompt}没有可用输入")
    return None


def calculate_bmi(weight, height):
    """计算 BMI；身高必须为正数，否则抛出 ValueError（避免除零）。"""
    if height <= 0:
        raise ValueError("身高必须大于 0")
    return weight / (height ** 2)


def main():
    print("===== 场景1：前面的输入非法，后面的合法 =====")
    weight = input_valid_number("请输入您的体重（单位：公斤）：", ["abc", "-5", "70"])
    height = input_valid_number("请输入您的身高（单位：米）：", ["1.75"])
    if weight is not None and height is not None:
        print(f"您的BMI是: {calculate_bmi(weight, height):.2f}")

    print("\n===== 场景2：全部输入都非法，返回 None =====")
    bad_weight = input_valid_number("请输入您的体重（单位：公斤）：", ["abc", "-1"])
    print(f"结果：{bad_weight}")

    print("\n===== 场景3：身高为 0，calculate_bmi 抛异常并处理 =====")
    try:
        calculate_bmi(70, 0)
    except ValueError as error:
        print(f"捕获到 ValueError：{error}")


if __name__ == "__main__":
    main()
