# 基础运算模块：提供加、减等基本数学运算的函数。
# 04_mymath_package_demo.py 会导入它。
# 运行自测：python python/exercises/03_modules_and_exceptions/mymath/basic.py


def add_numbers(x, y):
    """返回 x + y。"""
    return x + y


def subtract_numbers(x, y):
    """返回 x - y。"""
    return x - y


if __name__ == "__main__":
    print("===== mymath.basic 自测 =====")
    print(f"3 + 5 = {add_numbers(3, 5)}")
    print(f"10 - 4 = {subtract_numbers(10, 4)}")
