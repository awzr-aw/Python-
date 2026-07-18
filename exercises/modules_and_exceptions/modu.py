# modules_and_exceptions文件夹用于模块与异常处理练习
# 在这个文件夹中，你可以找到一些示例代码，用于练习如何编写和使用模块，以及如何处理异常。
# modu.py文件并非只有模块练习，也肯包含一些异常处理的示例代码。请根据需要进行练习。



#创建一个 utils.py 文件，里面写两个函数：celsius_to_fahrenheit(c) 将摄氏度转华氏度（公式：F = C * 9/5 + 32），fahrenheit_to_celsius(f) 将华氏度转摄氏度（公式：C = (F - 32) * 5/9）。在另一个 main.py 中，用 from utils import ... 导入这两个函数，调用并打印结果。
from utils import celsius_to_fahrenheit, fahrenheit_to_celsius

print(celsius_to_fahrenheit(30))  # 输出：86.0
print(fahrenheit_to_celsius(86))  # 输出：30.0