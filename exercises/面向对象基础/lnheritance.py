# 继承：实现代码的复用，通过继承可以将父类的属性和方法直接继承到子类中，子类可以新增专属属性或方法，也可以重写父类的方法
# 语法：
'''
class 类名(父类名1,父类名2,...):
    类体(可定义新属性/方法,或重写父类方法)
'''

# 定义父类(基类)
# class Animal:
#     # 父类的公有属性
#     def __init__(self,name):
#         self.name = name

#     # 父类的公有方法
#     def eat(self):
#         print(f"{self.name}正在吃东西")
#     def sleep(self):
#         print(f"{self.name}正在睡觉")

#     # 父类的私有方法
#     def __digest(self):
#         print(f"{self.name}正在消化食物")

# 定义子类(派生类)
# class Dog(Animal):
#     # 子类专属方法
#     def bark(self):
#         print(f"{self.name}正在汪汪汪叫")

# 创建子类对象
# dog = Dog() # 报错，因为继承父类，所以子类调用要写父类的参数
# dog = Dog("旺财")

# 子类复用父类的属性和方法
# dog.sleep()  # 调用父类的sleep方法
# # dog.__digest()  # 报错，因为私有方法不能被子类调用
# dog.eat()  # 调用父类的eat方法
# dog.bark()

# 继承作用
# 1. 实现代码的复用
# 2. 代码的扩展

# 方法重写，当父类的方法不能完全满足子类的需求时，可以重写父类的方法
# 语法：
'''
def 方法名(self,参数列表):
    # 方法体
'''

# class Animal:
#     def move(self):
#         print("动物在移动")


# class Bird(Animal):
#     # 重写父类方法(覆盖父类方法)
#     def move(self):
#         super().move()  # 调用父类的方法
#         print("鸟在飞翔")

# class Fish(Animal):
#     def move(self):
#         print("鱼在游泳")

# bird = Bird()
# fish = Fish()

# 调用move方法
# bird.move()  # 调用子类中定义的方法
# fish.move()

# 多重继承

class A:
    def func(self):
        print("A类的方法")

class B(A):
    def func(self):
        print("B类的方法")

class C(A):
    def func(self):
        print("C类的方法")

class D(B,C):
    def func(self):
        # print("D类的方法")
        pass

# 创建对象
d = D()
d.func()
print(D.__mro__)
# python中有内置属性__mro__明确方法的调用顺序，顺序为：子类，左侧父类，右侧父类，更上层父类，object
# 语法：类名.__mro__