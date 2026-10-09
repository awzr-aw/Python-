# 05_static_method_rectangle.py
# 【静态方法实战】用 @staticmethod 实现与对象状态无关的工具方法：矩形面积、周长。
# 来源：原 object_oriented/polypeptide.py 末尾的 Rectangle 部分。
# 运行：python python/exercises/05_object_oriented/05_static_method_rectangle.py
#
# 静态方法特点：
#   - 用 @staticmethod 装饰，第一个参数既不是 self 也不是 cls；
#   - 不依赖类和对象的状态，推荐用「类名.方法名(...)」调用；
#   - 好处：不用先创建对象，语义上也表明它只是「放在类里的小工具」。
#
# 修正说明：原方法名把 perimeter 拼错（少了字母 e），已改为 get_perimeter。


class Rectangle:
    """矩形工具类：面积和周长都只依赖传入的参数。"""

    @staticmethod
    def get_area(length, width):
        """返回矩形面积。"""
        return length * width

    @staticmethod
    def get_perimeter(length, width):
        """返回矩形周长（原方法名拼错，已修正为 get_perimeter）。"""
        return (length + width) * 2


def main():
    length, width = 5, 10
    print("===== 通过类名调用（推荐）=====")
    print(f"长={length}，宽={width}")
    print(f"面积 get_area = {Rectangle.get_area(length, width)}")            # 输出：50
    print(f"周长 get_perimeter = {Rectangle.get_perimeter(length, width)}")  # 输出：30

    print("\n===== 通过对象调用（允许但不推荐）=====")
    rectangle = Rectangle()
    print(f"rectangle.get_area = {rectangle.get_area(length, width)}")
    print(f"rectangle.get_perimeter = {rectangle.get_perimeter(length, width)}")

    print("\n对比：如果写成实例方法 def get_area(self, length, width)，就必须先创建对象才能用。")


if __name__ == "__main__":
    main()
