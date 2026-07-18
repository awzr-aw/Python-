# 我们要创建一个叫 mymath 的数学工具包
# 里面有基础运算和进阶运算两个模块，最后再写一个主程序来调用这个包里的功能
# 主程序入口。它会从 mymath 包里导入函数并使用，演示如何调用包内的功能
# 关联文件：
# mymath/basic.py
# mymath/advanced.py
# mymath/__init__.py

# # 主程序：演示如何导入和使用 mymath 包中的函数
from mymath.basic import add_numbers as add, subtract_numbers as subtract
from mymath.advanced import power

# 调用基础运算
print(f"3 + 5 = {add(3, 5)}")       # 应输出 8
print(f"10 - 4 = {subtract(10, 4)}") # 应输出 6

# 调用进阶运算
print(f"2的3次方 = {power(2, 3)}")     # 应输出 8


