#文件functions.py是函数相关练习文件


# 需求：定义一个函数 calculate_bmi(weight, height)，
# 参数是体重(kg)和身高(m)，返回BMI值。
# 再写一个函数 interpret_bmi(bmi)，根据BMI值返回体型描述（偏瘦、正常、偏重、肥胖）。
# 在主程序中调用这两个函数，输入身高体重，输出BMI值和体型描述。
# def calculate_bmi(weight, height):
#     bmi = weight / (height ** 2)
#     return bmi

# def interpret_bmi(bmi):
#     if bmi < 18.5:
#         return "偏瘦"
#     elif 18.5 <= bmi < 24.9:
#         return "正常"
#     elif 25 <= bmi < 29.9:
#         return "超重"
#     else:
#         return "肥胖"

# weight = float(input("请输入您的体重（单位：公斤）："))
# height = float(input("请输入您的身高（单位：米）："))
# bmi = calculate_bmi(weight, height)
# print(f"您的BMI值是：{bmi}")
# print(f"您的BMI状态是：{interpret_bmi(bmi)}")

# 需求：定义一个函数 analyze_weights(weights)，
# 参数是一个体重列表。函数返回三个值：平均体重、最高体重、最低体重。
# 在主程序中调用这个函数，用三个变量接收返回值，然后格式化输出。
# def analyze_weights(weights):
#     avg = sum(weights)/len(weights)
#     max_weight = max(weights)
#     min_weight = min(weights)
#     return avg, max_weight, min_weight
# weights = [70, 65, 80, 68, 72]
# avg, max_weight,min_weight = analyze_weights(weights)
# print(f"平均体重是：{avg}")
# print(f"最高体重是：{max_weight}")
# print(f"最低体重是：{min_weight}")

# 需求：升级第1题的BMI计算器。
# 定义一个函数 get_body_status(weight, height)，
# 它内部调用 calculate_bmi() 和 interpret_bmi()，
# 直接返回完整的体型描述字符串（如“你的BMI是22.5，属于正常范围”）。
# 主程序只需要调用 get_body_status() 这一个函数，传入数据就能拿到完整描述。
# def calculate_bmi(weight, height):
#     bmi = weight / (height ** 2)
#     return bmi

# def interpret_bmi(bmi):
#     if bmi < 18.5:
#         return "偏瘦"
#     elif 18.5 <= bmi < 24.9:
#         return "正常"
#     elif 25 <= bmi < 29.9:
#         return "超重"
#     else:
#         return "肥胖"

# def get_body_status(weight, height):
#     bmi = calculate_bmi(weight, height)
#     body_status = interpret_bmi(bmi)
#     return f"你的BMI是{bmi}，属于{body_status}范围"

# weight = float(input("请输入您的体重（单位：公斤）："))
# height = float(input("请输入您的身高（单位：米）："))
# print(get_body_status(weight, height))

# def calculate_bmi(weight, height):
#     bmi = weight / (height ** 2)
#     return bmi

# def get_body_status(weight, height):
#     def interpret_bmi(bmi):
#         if bmi < 18.5:
#             return "偏瘦"
#         elif 18.5 <= bmi < 24.9:
#             return "正常"
#         elif 25 <= bmi < 29.9:
#             return "超重"
#         else:
#             return "肥胖"

#     bmi = calculate_bmi(weight, height)
#     body_status = interpret_bmi(bmi)
#     return f"你的BMI是{bmi}，属于{body_status}范围"

# weight = float(input("请输入您的体重（单位：公斤）："))
# height = float(input("请输入您的身高（单位：米）："))
# print(get_body_status(weight, height))

# 需求：写一个函数 safe_int_convert(s)，
# 接受一个字符串参数，尝试将其转换为整数并返回。
# 如果转换失败，捕获 ValueError 并返回 None。调用这个函数，分别传入 "123"、"abc"、"45.6"，
# 打印返回结果

def safe_int_convert(s):
    try:
        return int(s)
    except ValueError:
        return None
print(safe_int_convert("123"))  # 输出：123
print(safe_int_convert("abc"))  # 输出：None
print(safe_int_convert("45.6"))  # 输出：None

#需求：写一个函数 divide_and_log(a, b)，接受两个数字，尝试计算 a / b。
# 如果除数为0，捕获 ZeroDivisionError 并打印 "除数不能为0"。如果计算成功，用 else 打印计算结果。
# 无论成功或失败，用 finally 打印 "运算结束"。
def divide_and_log(a, b):
    try:
        result =  a / b
        print("计算结果是：", result)
    except ZeroDivisionError:
        print("除数不能为0")
    else:
        print("计算成功")
    finally:
        print("运算结束")
divide_and_log(10, 2)  # 输出：计算结果是： 5.0
divide_and_log(10, 0)  # 输出：除数不能为0
divide_and_log(10, 3)  # 输出：计算结果是： 3.3333333333333335

