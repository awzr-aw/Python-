# 进阶运算模块：提供乘方等更复杂的数学运算函数。
# 04_mymath_package_demo.py 会导入它。
# 运行自测：python python/exercises/03_modules_and_exceptions/mymath/advanced.py


def power(base, exp):
    """返回 base 的 exp 次方。"""
    return base ** exp


if __name__ == "__main__":
    print("===== mymath.advanced 自测 =====")
    print(f"2的3次方 = {power(2, 3)}")
    print(f"5的0次方 = {power(5, 0)}")
