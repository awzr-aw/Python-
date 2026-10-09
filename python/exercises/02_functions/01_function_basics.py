# 01_function_basics.py
# 【函数基础】定义与调用、参数、返回值、作用域，以及函数里的异常处理。
# 来源：原 functions/functions.py（把同一个文件按题目分组整理，题面保留在注释里）。
# 运行：python python/exercises/02_functions/01_function_basics.py


# ---------- 题目 1：定义并调用函数 ----------
# 需求：定义一个 greet(name) 函数，返回问候语；在主程序里调用它。
def greet(name):
    """最简单的函数：接收参数，返回字符串。"""
    return f"你好，{name}！欢迎练习 Python 函数。"


# ---------- 题目 2：位置参数 / 默认参数 / 关键字参数 ----------
# 需求：定义一个 introduce(name, age=18, city="北京")，
#       分别用「省略默认值」「位置参数」「关键字参数」三种方式调用。
def introduce(name, age=18, city="北京"):
    return f"{name}，{age} 岁，来自{city}"


# ---------- 题目 3：返回多个值 ----------
# 需求：定义一个 min_max_avg(numbers)，一次返回（最小值, 最大值, 平均值）。
def min_max_avg(numbers):
    if not numbers:
        raise ValueError("列表不能为空")
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


# ---------- 题目 4：作用域 ----------
# 需求：观察局部变量和全局变量；在函数内修改全局变量要加 global。
counter = 0


def increase_counter():
    """global 声明后，函数内才能真正修改模块级变量。"""
    global counter
    counter += 1
    return counter


# ---------- 题目 5：safe_int_convert（原文件实现，保留） ----------
# 需求：写一个函数 safe_int_convert(s)，接受一个字符串参数，尝试将其转换为整数并返回。
#       如果转换失败，捕获 ValueError 并返回 None。
#       调用这个函数，分别传入 "123"、"abc"、"45.6"，打印返回结果。
def safe_int_convert(s):
    try:
        return int(s)
    except ValueError:
        return None


# ---------- 题目 6：divide_and_log（原文件实现，保留） ----------
# 需求：写一个函数 divide_and_log(a, b)，接受两个数字，尝试计算 a / b。
#       如果除数为 0，捕获 ZeroDivisionError 并打印 "除数不能为0"；
#       如果计算成功，用 else 打印计算结果；
#       无论成功或失败，用 finally 打印 "运算结束"。
def divide_and_log(a, b):
    try:
        result = a / b
        print("计算结果是：", result)
    except ZeroDivisionError:
        print("除数不能为0")
    else:
        print("计算成功")
    finally:
        print("运算结束")


def main():
    print("===== 题目1：定义并调用函数 =====")
    print(greet("小明"))

    print("\n===== 题目2：三种参数用法 =====")
    print(introduce("张三"))                        # 使用默认参数
    print(introduce("李四", 20))                    # 位置参数
    print(introduce(name="王五", city="上海"))      # 关键字参数

    print("\n===== 题目3：返回多个值 =====")
    min_value, max_value, avg_value = min_max_avg([70, 65, 80, 68, 72])
    print(f"最小值={min_value}，最大值={max_value}，平均值={avg_value}")

    print("\n===== 题目4：作用域 =====")
    print("第一次调用 increase_counter()：", increase_counter())
    print("第二次调用 increase_counter()：", increase_counter())

    print("\n===== 题目5：safe_int_convert =====")
    print(safe_int_convert("123"))    # 输出：123
    print(safe_int_convert("abc"))    # 输出：None
    print(safe_int_convert("45.6"))   # 输出：None

    print("\n===== 题目6：divide_and_log =====")
    divide_and_log(10, 2)   # 计算结果是 5.0 / 计算成功 / 运算结束
    divide_and_log(10, 0)   # 除数不能为0 / 运算结束
    divide_and_log(10, 3)   # 计算结果是 3.333... / 计算成功 / 运算结束


if __name__ == "__main__":
    main()
