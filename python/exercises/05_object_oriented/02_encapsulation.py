# 02_encapsulation.py
# 【封装】把对象的属性和方法隐藏起来，只暴露必要的接口给外部使用。
# 来源：原 object_oriented/encapsulation.py。
# 运行：python python/exercises/05_object_oriented/02_encapsulation.py
#
# 封装通过访问控制定义属性 / 方法的可访问范围，Python 遵循「约定优于强制」：
# 以双下划线开头（且不以双下划线结尾）的成员会被「名称改写」成 _类名__成员名，
# 所以外部无法用 p.__age 直接访问，但通过改写后的名字仍然可以强访问（不推荐）。
#
# 修正说明：原文件里定义了两次 class Person（后者覆盖前者），还散落着几处顶层 print，
# 直接运行时只有最后一段生效、前面的示例看不到结果。这里拆成两个名字不同的类，
# 所有演示都收进函数，由 if __name__ == "__main__" 统一调用。


class Person:
    """方式一：用公开的 getter() / setter() 方法访问私有属性。"""

    def __init__(self, name, age):
        self.name = name        # 公共属性
        self.__age = age        # 私有属性（名称会被改写成 _Person__age）

    def getter(self):
        """获取私有属性。"""
        return self.__age

    def setter(self, age):
        """设置私有属性，并做范围校验。"""
        if 0 < age < 120:
            self.__age = age
        else:
            print(f"年龄 {age} 不在合理范围内，保持原值 {self.__age}")

    def say_hello(self):
        # 类内部可以自由访问私有属性
        print(f"你好，我的名字是 {self.name}，今年{self.__age}岁")


class PersonProperty:
    """方式二：用 @property 装饰器把方法「伪装」成属性，使用起来更自然。"""

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        # 获取器：被 @property 装饰的方法名会被当作属性名，访问时不用加括号
        return self.__age

    @age.setter
    def age(self, age):
        # 设置器：方法名必须与获取器一致，赋值时自动触发校验
        if 0 < age < 120:
            self.__age = age
            print(f"年龄设置成功，当前年龄为 {self.__age}")
        else:
            print("年龄不在合理范围内")

    @age.deleter
    def age(self):
        # 删除器：del 属性时触发
        del self.__age
        print("年龄已删除")


def show_getter_setter():
    print("===== 1. getter / setter 方式 =====")
    person = Person("Alice", 30)
    print(f"初始年龄：{person.getter()}")
    person.setter(31)
    print(f"修改后年龄：{person.getter()}")
    person.setter(150)      # 超出范围，保持原值
    person.say_hello()
    print("提示：外部直接写 person.__age 会报 AttributeError（这里不触发，避免脚本中断）")


def show_property():
    print("\n===== 2. @property 方式 =====")
    person = PersonProperty("Bob", 28)
    print(f"读取属性：person.age = {person.age}")   # 访问属性不用加括号
    person.age = 31                                  # 触发 setter
    print(f"赋值后：person.age = {person.age}")
    person.age = 150                                 # 触发 setter 的范围校验
    del person.age                                   # 触发 deleter
    print("提示：del 之后再读 person.age 会报 AttributeError（这里不再读取）")


def show_name_mangling():
    print("\n===== 3. 名称改写（私有属性的真实存储名）=====")
    person = Person("Alice", 30)
    private_names = [name for name in dir(person) if "age" in name]
    print(f"dir(person) 里和 age 有关的名字：{private_names}")
    print(f"强制访问 _Person__age = {person._Person__age}   # 不推荐，只是为了看清机制")


def main():
    show_getter_setter()
    show_property()
    show_name_mangling()


if __name__ == "__main__":
    main()
