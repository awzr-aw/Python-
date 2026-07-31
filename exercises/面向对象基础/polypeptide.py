# 多态&类方法&静态方法
# 多态：同一接口下，不同的实现，易扩展
# (1)鸭子类型：鸭子类型是指，如果一个对象的行为符合某个接口，那么它就可以被当作这个接口的实例来使用。
# 定义猫类
# class Cat:
#     def make_sound(self):
#         print("猫咪：喵喵喵~")
# # 定义狗类
# class Dog:
#     def make_sound(self):
#         print("狗狗：汪汪汪~")
# # 定义闹钟类
# class AlarmClock:
#     def make_sound(self):
#         print("闹钟：滴答滴答~")
# # 定义玩具恐龙类
# class ToyDinosaur:
#     def make_sound(self):
#         print("玩具恐龙：咯咯咯~")

# # 定义统一接口(函数),同一方法，传入不同对象，产生不同结果
# def let_it_shout(sound_object):
#     sound_object.make_sound()

# # 创建对象
# cat = Cat()
# dog = Dog()
# alarm_clock = AlarmClock()
# toy_dinosaur = ToyDinosaur()

# # 调用统一接口
# let_it_shout(cat)  # 输出：猫咪：喵喵喵~
# let_it_shout(dog)  # 输出：狗狗：汪汪汪~
# let_it_shout(alarm_clock)  # 输出：闹钟：滴答滴答~
# let_it_shout(toy_dinosaur)  # 输出：玩具恐龙：咯咯咯~

# (2)继承+方法重写：继承+方法重写，子类可以重写父类的方法，子类的方法会覆盖父类的方法。
# 与鸭子类型类似，好处在于可以super()调用，并且如果pass子类方法，那么子类会直接用父类的方法
# 定义动物类
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def make_sound(self):
#         print(f"{self.name}发出声音")
# # 定义猫类，继承自Animal类
# class Cat(Animal):
#     def make_sound(self):
#         print(f"{self.name}发出喵喵喵的声音")
# # 定义狗类，继承自Animal类
# class Dog(Animal):
#     def make_sound(self):
#         print(f"{self.name}发出汪汪汪的声音")
# # 定义闹钟类，继承自Animal类
# class AlarmClock(Animal):
#     def make_sound(self):
#         print(f"{self.name}发出滴答滴答的声音")
# # 定义玩具恐龙类，继承自Animal类
# class ToyDinosaur(Animal):
#     def make_sound(self):
#         print(f"{self.name}发出咯咯咯的声音")

# # 统一接口
# def animal_sound(animal):
#     animal.make_sound()



# 调用统一接口
# animal_sound(Cat("小花"))
# animal_sound(Dog("小黑"))
# animal_sound(AlarmClock("闹钟"))
# animal_sound(ToyDinosaur("玩具恐龙"))


# 类方法，需要用到装饰器
# 类方法使用@classmethod装饰器,类方法的第一个参数是cls(类)，表示类本身，通常命名为cls

'''
在类中定义方法分两种：
绑定方法：
    特殊之处就是把调用者当作参数进行传递，传递给方法的第一个参数是调用者本身。
        绑定给对象的方法：实例方法(self)调用者是对象，自动当作参数
        绑定给类的方法：类方法(cls)调用者是类，自动当作参数
非绑定方法：
    类与对象不绑定
        静态方法，默认没有必须传递的参数
'''
# 语法：
'''
@classmethod
def 方法名(cls, 参数):
    方法体
调用方式：
推荐通过类名调用
'类名.方法名(参数)'
允许但不推荐用对象调用
'对象名.方法名(参数)'
'''

# class Person:
#     @classmethod
#     def walk(cls):
#         print(f"人类{cls}正在走路")

# # 通过类名调用
# Person.walk()
# print(f"类本身：{Person}")

# # 通过对象调用
# p1 = Person()
# p1.walk()
# print(f"对象本身：{p1}") # 会输出类型和十六进制地址


# 应用场景
# 1.访问和修改类属性
# class Person:
#     country = "中国"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def set_country(cls, new_country):
#         # print(Person.country)# 可维护性太低不推荐使用
#         print(cls.country) # 推荐
#         # 修改类属性
#         cls.country = new_country
#         print(f"{cls}类的国家属性已修改为：{cls.country}")

# Person.set_country("美国")
# Person.set_country("英国")

# 2.类方法中创建对象
class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

    def __str__(self):
        # 自定义对象的输出格式
        return f"书名：{self.name}, 作者：{self.author}, 价格：{self.price}元"
    @classmethod
    def from_string(cls,book_info):
        # 解析字符串，拆分出书名、作者、价格(分割后解包)
        name,author,price = book_info.split("-")
        price = float(price)  # 转换为浮点数

        # 创建对象,类名(),使用cls(代表类本身)创建对象
        book_obj = cls(name,author,price)
        # 返回对象
        return book_obj


# 假设在网上爬取一个信息
# "Python入门-李四-100"
print(Book.from_string("Python入门-李四-100"))