# utils_temperature.py
# 【模块】温度转换工具模块：摄氏度 <-> 华氏度。
# 被同目录的 01_temperature_converter.py 用 `from utils_temperature import ...` 导入。
# 运行：python python/exercises/03_modules_and_exceptions/utils_temperature.py
#
# 操作说明（原 modules_and_exceptions/utils.py 的题面）：
#   创建一个 utils.py 文件，里面写两个函数：
#   celsius_to_fahrenheit(c) 将摄氏度转华氏度（公式：F = C * 9/5 + 32），
#   fahrenheit_to_celsius(f) 将华氏度转摄氏度（公式：C = (F - 32) * 5/9）。
#   在另一个文件中用 from utils import ... 导入这两个函数，调用并打印结果。
#
# 改动说明：模块名从 utils.py 改为 utils_temperature.py（名字更明确，也避免与别的 utils 重名），
# 并把原来的参数名 F/c 统一成小写的完整单词，避免同名变量大小写混用。


def celsius_to_fahrenheit(celsius):
    """摄氏度 -> 华氏度：F = C * 9 / 5 + 32"""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """华氏度 -> 摄氏度：C = (F - 32) * 5 / 9"""
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    print("===== utils_temperature 模块自测 =====")
    print(f"37 摄氏度 = {celsius_to_fahrenheit(37):.1f} 华氏度")
    print(f"98.6 华氏度 = {fahrenheit_to_celsius(98.6):.1f} 摄氏度")
