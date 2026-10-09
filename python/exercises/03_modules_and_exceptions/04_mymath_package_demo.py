# 04_mymath_package_demo.py
# 【包与模块】演示如何导入自己写的 mymath 包。
# 来源：原 modules_and_exceptions/main.py + mymath/*。
# 运行：python python/exercises/03_modules_and_exceptions/04_mymath_package_demo.py
#
# 目录结构：
#   mymath/__init__.py   包说明
#   mymath/basic.py      基础运算：加、减
#   mymath/advanced.py   进阶运算：乘方
# Python 会把脚本所在目录加入模块搜索路径，所以这里的 mymath 可以直接导入，
# 与当前工作目录无关。

import mymath
from mymath.advanced import power
from mymath.basic import add_numbers as add, subtract_numbers as subtract


def main():
    print("===== 基础运算 =====")
    print(f"3 + 5 = {add(3, 5)}")           # 应输出 8
    print(f"10 - 4 = {subtract(10, 4)}")    # 应输出 6

    print("\n===== 进阶运算 =====")
    print(f"2的3次方 = {power(2, 3)}")       # 应输出 8
    print(f"5的0次方 = {power(5, 0)}")       # 应输出 1

    print("\n===== 包的元信息 =====")
    print(f"mymath 包定义文件：{mymath.__file__}")


if __name__ == "__main__":
    main()
