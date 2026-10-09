# 01_temperature_converter.py
# 【模块导入】把工具函数放进单独模块，再在另一个文件里导入使用。
# 来源：原 modules_and_exceptions/modu.py（调用方）+ utils.py（工具模块）。
# 运行（在仓库根执行）：python python/exercises/03_modules_and_exceptions/01_temperature_converter.py
#
# 导入要点：
#   - Python 运行脚本时会自动把「脚本所在目录」加入模块搜索路径，
#     所以这里可以直接 `from utils_temperature import ...`，与当前工作目录无关；
#   - 导入时不会执行被导入模块里 `if __name__ == "__main__":` 下面的自测代码，
#     这正是每个文件都写入口判断的原因。

from utils_temperature import celsius_to_fahrenheit, fahrenheit_to_celsius


def convert_and_report(celsius):
    """转成华氏度后再转回来，验证两个函数互为逆运算。"""
    fahrenheit = celsius_to_fahrenheit(celsius)
    back = fahrenheit_to_celsius(fahrenheit)
    return f"{celsius} 摄氏度 = {fahrenheit:.1f} 华氏度（再转回来 = {back:.1f} 摄氏度）"


def main():
    print("===== 1. 直接调用导入的函数 =====")
    print(celsius_to_fahrenheit(30))   # 输出：86.0
    print(fahrenheit_to_celsius(86))   # 输出：30.0

    print("\n===== 2. 组装成小报告 =====")
    for value in (0, 30, 37, 100):
        print(convert_and_report(value))


if __name__ == "__main__":
    main()
