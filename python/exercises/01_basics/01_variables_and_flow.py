# 01_variables_and_flow.py
# Python 基础第一篇：变量、数据类型、运算符、输入输出、条件判断与循环。
# 来源：原 basics/basics.py 是一个「全是注释、跑不出结果」的笔记文件，
# 这里保留原来的中文知识注释，并在下面补上可运行代码，运行后能直接看到结论。
# 运行：python python/exercises/01_basics/01_variables_and_flow.py


# ---------- 1. 变量与基本数据类型 ----------
# 变量不需要提前声明类型，赋值即创建，类型由值决定。
# 常见类型：int 整数、float 浮点数、str 字符串、bool 布尔值、NoneType 空值。
name = "小明"
age = 20
height = 1.75
is_student = True
nothing = None


def describe_variables():
    """打印变量及其类型，直观看到 Python 是动态类型语言。"""
    for value in (name, age, height, is_student, nothing):
        print(f"值={value!r:<10}类型={type(value).__name__}")


# ---------- 2. 运算符 ----------
def show_operators():
    print("7 + 2 =", 7 + 2)
    print("7 - 2 =", 7 - 2)
    print("7 * 2 =", 7 * 2)
    print("7 / 2 =", 7 / 2)      # 真除法，结果一定是 float
    print("7 // 2 =", 7 // 2)    # 整除（向下取整）
    print("7 % 2 =", 7 % 2)      # 取余
    print("7 ** 2 =", 7 ** 2)    # 幂运算
    print("3 > 2 and 1 < 2 ->", 3 > 2 and 1 < 2)
    print("not is_student ->", not is_student)


# ---------- 3. 输入输出与类型转换 ----------
# input("提示") 会从键盘读取一行、返回字符串。注意：它会阻塞等待输入，
# 所以自动运行的脚本里不要用它；这里用固定字符串模拟一次输入。
def fake_input(prompt, raw_value):
    """模拟 input()：打印提示后返回固定字符串，保证脚本不会卡住。"""
    print(f"{prompt}{raw_value}   <- 模拟输入")
    return raw_value


def convert_types():
    raw_weight = fake_input("请输入您的体重（单位：公斤）：", "65.5")
    weight = float(raw_weight)          # 字符串 -> 浮点数
    print(f"转换后：{weight}（{type(weight).__name__}）；取整后：{int(weight)}")
    print(f"格式化输出：体重 {weight:.1f} kg")


# ---------- 4. 条件判断 ----------
def judge_bmi(bmi):
    """按中国成人标准判断体型，if/elif/else 从上到下只会命中一个分支。"""
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 24.0:
        return "正常"
    elif bmi < 28.0:
        return "超重"
    else:
        return "肥胖"


# ---------- 5. 循环 ----------
def show_loops():
    total = 0
    for i in range(1, 6):        # range(1, 6) 生成 1,2,3,4,5（左闭右开）
        total += i
    print("1~5 求和：", total)

    count = 0
    while count < 3:
        count += 1
    print("while 循环执行次数：", count)

    for n in range(1, 10):
        if n == 3:
            continue             # 跳过本次，直接进入下一次循环
        if n == 6:
            break                # 结束整个循环
        print("for + break/continue 输出：", n)


def main():
    print("===== 1. 变量与类型 =====")
    describe_variables()
    print("\n===== 2. 运算符 =====")
    show_operators()
    print("\n===== 3. 类型转换与格式化 =====")
    convert_types()
    print("\n===== 4. 条件判断 =====")
    for bmi in (17.0, 22.0, 26.0, 30.0):
        print(f"BMI {bmi} -> {judge_bmi(bmi)}")
    print("\n===== 5. 循环 =====")
    show_loops()


if __name__ == "__main__":
    main()
