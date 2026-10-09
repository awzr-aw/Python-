# 01_class_basics.py
# 【面向对象基础】类的定义、对象（实例）、实例方法、类属性、实例属性、构造方法、魔术方法。
# 来源：原 object_oriented/class_pass.py（原文全篇是注释，这里保留知识注释并补上可运行示例）。
# 运行：python python/exercises/05_object_oriented/01_class_basics.py
#
# 类的定义（类是对一系列具有相同属性和方法的对象的抽象描述）：
#   class 类名:
#       类体
# 对象的定义（对象是类的实例）：
#   对象名 = 类名()


class EmptyPerson:
    """空类：类体里只放一句文档字符串，就是一个合法（但不做事）的类。"""


class Person:
    """演示实例方法、类属性、实例属性和构造方法。"""

    # 类属性：定义在类中、所有方法体之外，所有对象共享，推荐用「类名.属性名」访问。
    country = "中国"
    hair_color = "黑色"

    def __init__(self, name, age):
        # 构造方法：创建对象时自动调用，用来初始化实例属性（定义实例属性的最佳方式）。
        print(f"我是构造方法，正在初始化 {name} 的属性。")
        self.name = name      # 实例属性：绑定到具体对象，每个对象独立
        self.age = age

    def speak(self):
        # 实例方法：第一个参数必须是 self，代指调用该方法的对象。
        # 实例方法只能由对象调用；Person.speak(person) 这种手动传参的方式也可以。
        print(f"{self.name} 会说话")

    def introduce(self):
        print(f"我是{self.name}，今年{self.age}岁，住在{self.country}，头发是{self.hair_color}色。")

    def __str__(self):
        # 魔术方法：重写后 print(对象) / f-string 会输出自定义的友好字符串（必须返回字符串）。
        return f"姓名:{self.name},年龄:{self.age}"

    def __del__(self):
        # 析构方法：对象不再被引用时自动调用，用来做收尾工作。
        print(f"对象{self.name}销毁，释放内存空间")


def show_class_and_object():
    print("===== 1. 类与对象 =====")
    print(f"空类实例：{EmptyPerson()}   # 默认输出类型和内存地址")
    person1 = EmptyPerson()
    person2 = EmptyPerson()
    print(f"两个对象是否相等（==）：{person1 == person2}   # 地址不同，所以是 False")
    print(f"两个对象是否同一（is）：{person1 is person2}   # 也是 False")


def show_instance_method():
    print("\n===== 2. 实例方法与 self =====")
    zhangsan = Person("张三", 20)
    zhangsan.speak()             # 对象调用：自动把 zhangsan 传给 self
    Person.speak(zhangsan)       # 非绑定调用：手动把对象传进去，效果相同
    try:
        Person.speak()           # 缺少 self 参数，会报错
    except TypeError as error:
        print(f"Person.speak() 直接调用会报错：{error}")


def show_class_attribute():
    print("\n===== 3. 类属性（所有对象共享）=====")
    print(f"Person.country = {Person.country}")
    p1 = Person("李四", 25)
    p2 = Person("王五", 26)
    print(f"通过对象访问（不推荐）：p1.country = {p1.country}")
    Person.country = "美国"          # 只能通过类名修改类属性
    print(f"通过类名修改后：Person.country = {Person.country}")
    p1.country = "日本"              # 只是给 p1 新建了同名实例属性，不影响类属性
    print(f"p1.country（实例属性）= {p1.country}")
    print(f"p2.country（仍是类属性）= {p2.country}")
    print(f"Person.country（类属性没变）= {Person.country}")


def show_instance_attribute():
    print("\n===== 4. 实例属性（每个对象各自一份，互不影响）=====")
    p1 = Person("张三", 20)
    p2 = Person("李四", 25)
    p1.name = "王五"                 # 修改 p1 的实例属性
    print(f"p1.name = {p1.name}（已修改）")
    print(f"p2.name = {p2.name}（不受影响）")


def show_special_methods():
    print("\n===== 5. 魔术方法 __str__ / __del__ =====")
    person = Person("赵六", 22)
    print(person)                                  # 自动调用 __str__
    print(f"f-string 里也会调用 __str__：{person}")
    del person                                     # 手动删除对象，立即触发 __del__
    print("del 之后对象已销毁（再访问会 NameError，这里不再演示）")


def main():
    show_class_and_object()
    show_instance_method()
    show_class_attribute()
    show_instance_attribute()
    show_special_methods()


if __name__ == "__main__":
    main()
