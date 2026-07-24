# 封装与继承
# 封装：将对象的属性和方法隐藏起来，只暴露必要的接口给外部使用
# 继承：实现代码的复用，通过继承可以将父类的属性和方法直接继承到子类中，子类可以新增专属属性或方法，也可以重写父类的方法

# 封装主要通过访问控制定义(属性/方法)的可访问范围，在python里遵循(约定优于强制)
# 约定属性/方法名前加上双下划线(__)表示私有属性/方法，外部无法直接访问
# class Person:
#     def __init__(self, name, age):
#         self.name = name  # 公共属性
#         self.age = age

#     def sey_hello(self):
#         print("Hello, my name is " + self.name)

# print(name) # 报错，外部不可以直接访问类属性
# print(sey_hello()) # 报错，外部不可以直接访问类方法

# 创建对象，对象就可以看作是一个简单接口
# person = Person("Alice", 30)
# person.sey_hello()  # 输出：Hello, my name is Alice
# 开放性，外部可以随意查看和修改对象的属性，安全性较低

# 定义私有，在属性/方法名前加上双下划线(__)，外部无法直接访问
# class Person:
#     def __init__(self, name, age):
#         self.name = name  # 公共属性
#         self.__age = age  # 私有属性

#     def sey_hello(self):
#         print(f"你好，我的名字是 {self.name}今年{self.__age}岁")
        # 在类内部，可以访问私有属性
# p = Person("Alice", 30)
# print(p.name)  # 输出：Alice
# # print(p.__age)  # 报错，外部无法直接访问私有属性
# p.sey_hello() # 输出：你好，我的名字是 Alice今年30岁
# 封装后，外部只能通过接口访问对象的属性和方法，安全性较高

# 访问私有属性
# (1)类中定义公开的getter()和setter()方法，用于访问和修改私有属性
class Person:
    def __init__(self, name, age):
        self.name = name  # 公共属性
        self.__age = age  # 私有属性

    # 定义公开方法
    # 获取私有属性
    def getter(self):
        return self.__age
    # 设置私有属性
    def setter(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            print("年龄不在合理范围内")

# 通过公开的方法访问私有属性
p = Person("Alice", 30)
print(p.getter())  # 输出：30
p.setter(31)
print(p.getter())  # 输出：31

# (2)property装饰器，简化getter()和setter()方法的定义
# @property是python中用于将类方法"伪装"成属性的装饰器
# 它允许通过类似访问属性的语法访问方法
# 支持添加自定义的获取，设置和删除逻辑
# 语法：
# 1.获取器: 用@property装饰"获取方法"，被装饰的方法名会被当作属性名
# 2.设置器: 用@方法名.setter装饰"设置方法"
# 3.删除器: 用@方法名.deleter装饰"删除方法"
# 三者方法名必须一致

class Person:
    def __init__(self, name, age):
        self.name = name  
        self.__age = age  # 私有属性
    # 获取器,被装饰的方法名会被当作属性名
    @property
    def age(self):
        return self.__age
    # 设置器
    @age.setter
    def age(self, age):
        if 0 < age < 120:
            self.__age = age
            print(f"年龄设置成功,当前年龄为{self.__age}")
        else:
            print("年龄不在合理范围内")

    # 删除器
    @age.deleter
    def age(self):
        del self.__age
        print("年龄已删除")

p = Person("Alice", 30)
print(p.age)  # 访问属性不用加括号
p.age = 31
print(p.age)  # 输出：31
p.age = 150  # 输出：年龄不在合理范围内
del p.age  # 输出：年龄已删除
# print(p.age)  # 报错

# (3)内部改写机制，不推荐
# 在类内部，可以通过self.__class__.__setattr__(self, name, value)来改写属性
# 强烈建议在类内部使用property装饰器，而不是直接改写属性

