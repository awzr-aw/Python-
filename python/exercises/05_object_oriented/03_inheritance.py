# 03_inheritance.py
# 【继承】子类复用父类的属性和方法，也可以新增专属方法或重写父类方法。
# 来源：原 object_oriented/lnheritance.py（多重继承 / MRO 部分拆到 06_multiple_inheritance_mro.py）。
# 运行：python python/exercises/05_object_oriented/03_inheritance.py
#
# 语法：
#   class 类名(父类名1, 父类名2, ...):
#       类体（可定义新属性 / 方法，或重写父类方法）
#
# 修正说明：原文件写的是
#       class Dog(Animal):
#           dog = Dog()
#   存在两个问题：一是创建对象写进了类体里（一导入就执行），
#   二是 Dog 没有实现父类构造方法要求的 name 参数，直接调用会 TypeError。
#   这里改成在演示函数里 Dog("旺财") 创建对象。


class Animal:
    """父类（基类）：提供 name 属性和 eat / sleep / move 公共方法。"""

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}正在吃东西")

    def sleep(self):
        print(f"{self.name}正在睡觉")

    def move(self):
        print(f"{self.name}在移动")

    def __digest(self):
        # 私有方法：名称会被改写成 _Animal__digest，子类和外部都不能直接调用
        print(f"{self.name}正在消化食物")


class Dog(Animal):
    """子类（派生类）：继承 Animal，并新增专属方法 bark。"""

    def bark(self):
        print(f"{self.name}正在汪汪汪叫")


class Bird(Animal):
    """重写父类方法：先用 super() 执行父类逻辑，再补充自己的逻辑。"""

    def move(self):
        super().move()          # 调用父类的 move
        print(f"{self.name}在飞翔")


class Fish(Animal):
    """重写父类方法：完全覆盖父类实现。"""

    def move(self):
        print(f"{self.name}在游泳")


def show_inheritance():
    print("===== 1. 继承与代码复用 =====")
    dog = Dog("旺财")            # 必须传入父类构造方法要求的 name
    dog.eat()                    # 复用父类的 eat
    dog.sleep()                  # 复用父类的 sleep
    dog.bark()                   # 子类专属方法
    print("继承的作用：1) 代码复用；2) 便于扩展。")
    print("提示：dog.__digest() 会报 AttributeError，私有方法不能被子类访问。")


def show_override():
    print("\n===== 2. 方法重写（覆盖父类方法）=====")
    bird = Bird("小鸟")
    fish = Fish("小鱼")
    bird.move()                  # 输出：小鸟在移动 + 小鸟在飞翔
    fish.move()                  # 完全覆盖，只输出：小鱼在游泳


def main():
    show_inheritance()
    show_override()


if __name__ == "__main__":
    main()
