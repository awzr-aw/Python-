# 04_polymorphism.py
# 【多态 & 类方法 / 静态方法】同一接口、不同实现；绑定方法与「非绑定」方法的区别。
# 来源：原 object_oriented/polypeptide.py（Rectangle 静态方法部分拆到 05_static_method_rectangle.py）。
# 运行：python python/exercises/05_object_oriented/04_polymorphism.py
#
# 多态：同一个接口（函数 / 方法名）下有不同的实现，调用方不用关心具体类型，易扩展。
# 两种常见做法：
#   1) 鸭子类型：不要求继承，只要有同样的方法就能被当接口使用；
#   2) 继承 + 方法重写：子类覆盖父类方法，好处是可以用 super() 复用父类逻辑。


# ---------- 1. 鸭子类型：只要方法名对得上就能用 ----------
class Cat:
    def make_sound(self):
        print("猫咪：喵喵喵~")


class Dog:
    def make_sound(self):
        print("狗狗：汪汪汪~")


class AlarmClock:
    def make_sound(self):
        print("闹钟：滴答滴答~")


class ToyDinosaur:
    def make_sound(self):
        print("玩具恐龙：咯咯咯~")


# ---------- 2. 继承 + 方法重写 ----------
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name}发出声音")


class HouseCat(Animal):
    def make_sound(self):
        print(f"{self.name}发出喵喵喵的声音")


class Watchdog(Animal):
    def make_sound(self):
        print(f"{self.name}发出汪汪汪的声音")


class DigitalClock(Animal):
    def make_sound(self):
        print(f"{self.name}发出滴答滴答的声音")


class RobotDinosaur(Animal):
    def make_sound(self):
        print(f"{self.name}发出咯咯咯的声音")


# ---------- 3. 类方法 @classmethod ----------
class Person:
    """类方法：第一个参数是 cls（类本身），推荐用「类名.方法名()」调用。"""

    country = "中国"

    def __init__(self, name):
        self.name = name

    @classmethod
    def walk(cls):
        print(f"人类{cls}正在走路")

    @classmethod
    def set_country(cls, new_country):
        # 用 cls 访问 / 修改类属性：可维护性比写死类名高，也更利于继承
        print(f"修改前：{cls.country}")
        cls.country = new_country
        print(f"{cls}类的国家属性已修改为：{cls.country}")


class Book:
    """类方法的典型用途：充当「备选构造方法」，从别的格式创建对象。"""

    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

    def __str__(self):
        return f"书名：{self.name}, 作者：{self.author}, 价格：{self.price}元"

    @classmethod
    def from_string(cls, book_info):
        # 假设从网页上爬到的信息形如 "Python入门-李四-100"
        name, author, price = book_info.split("-")
        return cls(name, author, float(price))


# ---------- 4. 静态方法 @staticmethod（入门，详见 05_static_method_rectangle.py） ----------
class StaticDemo:
    @staticmethod
    def walk():
        print("正在行走")


def show_duck_typing():
    print("===== 1. 鸭子类型 =====")

    def let_it_shout(sound_object):
        sound_object.make_sound()

    for sound_object in (Cat(), Dog(), AlarmClock(), ToyDinosaur()):
        let_it_shout(sound_object)


def show_inheritance_polymorphism():
    print("\n===== 2. 继承 + 方法重写 =====")
    animals = (HouseCat("小花"), Watchdog("小黑"), DigitalClock("闹钟"), RobotDinosaur("玩具恐龙"))
    for animal in animals:
        animal.make_sound()


def show_class_method():
    print("\n===== 3. 类方法 @classmethod =====")
    Person.walk()                 # 推荐：通过类名调用
    print(f"类本身：{Person}")
    person = Person("张三")
    person.walk()                 # 允许但不推荐：通过对象调用，cls 仍然是 Person
    print(f"对象本身：{person}")

    Person.set_country("美国")
    Person.set_country("英国")

    print("\n用类方法从字符串创建对象：")
    print(Book.from_string("Python入门-李四-100"))


def show_static_method():
    print("\n===== 4. 静态方法 @staticmethod（入门）=====")
    StaticDemo.walk()             # 推荐：通过类名调用
    StaticDemo().walk()           # 通过对象调用也允许，但没有任何意义


def show_binding_conclusion():
    print("\n===== 5. 结论：绑定方法 vs 非绑定方法 =====")
    print("绑定方法：调用者本身会作为第一个参数自动传入。")
    print("  - 实例方法：绑定对象，第一个参数是 self（对象）；object.method() 会自动补 self。")
    print("  - 类方法：绑定类，第一个参数是 cls（类）；Class.method() 会自动补 cls。")
    print("非绑定方法：静态方法，没有 self / cls，类和对象都能调用，但调用者不会作为参数传入。")


def main():
    show_duck_typing()
    show_inheritance_polymorphism()
    show_class_method()
    show_static_method()
    show_binding_conclusion()


if __name__ == "__main__":
    main()
