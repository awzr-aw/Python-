# 多态&类方法&静态方法
# 多态：同一接口下，不同的实现
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
# 定义动物类
class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print(f"{self.name}发出声音")
# 定义猫类，继承自Animal类
class Cat(Animal):
    def make_sound(self):
        print(f"{self.name}发出喵喵喵的声音")
# 定义狗类，继承自Animal类
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name}发出汪汪汪的声音")
# 定义闹钟类，继承自Animal类
class AlarmClock(Animal):
    def make_sound(self):
        print(f"{self.name}发出滴答滴答的声音")
# 定义玩具恐龙类，继承自Animal类
class ToyDinosaur(Animal):
    def make_sound(self):
        print(f"{self.name}发出咯咯咯的声音")

# 统一接口
def animal_sound(animal):
    animal.make_sound()



# 调用统一接口
animal_sound(Cat("小花"))
animal_sound(Dog("小黑"))
animal_sound(AlarmClock("闹钟"))
animal_sound(ToyDinosaur("玩具恐龙"))


