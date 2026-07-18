# 第一题：带异常处理的BMI计算器升级版。
# 定义一个函数 input_valid_number(prompt)，反复提示用户输入数字，直到输入合法为止（捕获 ValueError）
# 定义一个函数 calculate_bmi(weight, height) 计算BMI
# 主程序调用 input_valid_number 获取体重和身高，再调用 calculate_bmi 计算并输出结果
# 如果用户输入了负数，用 raise 抛出 ValueError 并提示 "数值不能为负数"
def input_valid_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            if num < 0:
                raise ValueError("数值不能为负数")
            return num
        except ValueError as e:# ValueError 是输入无效时抛出的异常
            print(e)
def  calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
input_weight = input_valid_number("请输入您的体重（单位：公斤）：")
input_height = input_valid_number("请输入您的身高（单位：米）：")
bmi = calculate_bmi(input_weight, input_height)
print(f"您的BMI是: {bmi}")