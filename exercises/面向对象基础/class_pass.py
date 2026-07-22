# 面向对象与类基础
# 类的定义:
# 类是对一系列具有相同属性和方法的对象的抽象描述。
# 语法:
'''
class 类名:
    类体
'''

# class Person:
#     pass   # 空语句，不执行任何操作，可以用作占位符

# 对象的定义:
# 对象是类的实例，通过类创建的对象称为实例。
# 语法:
'''
对象名 = 类名()
'''
# print(Person())  # 输出对象的类型和十六进制地址
# print(Person())  # 创建多个对象，地址不同
# 为了方便，可以给对象起名字
# person1 = Person()
# person2 = Person()
# print(person1)  # 输出对象的类型和十六进制地址
# print(person2)  # 输出对象的类型和十六进制地址
# print(person1 == person2)  # 输出False，因为对象地址不同
# print(person1 is person2)  # 输出False，因为对象地址不同

# 在类中定义实例方法
# 实例方法是定义在类中的函数，用于描述对象的行为或功能实现，实例方法只能对象调用
# 语法:
'''
class 类名:
    def 方法名(self, 参数):
        方法体
        return 返回值
'''
# 特征:
# 1.强制包含self参数，表示调用该方法的对象，会自动绑定调用该方法的对象
# 便于在方法体内访问和修改对象的属性和状态
# 2.实例方法只能对象调用，语法：对象名.方法名(参数)
# class Person:
#     def speak(self):
#         print(f"{self}会说话")  # self指代调用该方法的对象，self命名不强制，但不推荐更换
        # self仅在实例方法内部有效

# zhangsan = Person()
# print(f"张三:{zhangsan}")
# 调用实例方法
# Person.speak()  # 报错，因为speak方法是实例方法，只能对象调用，可以写成Person.speak(zhangsan)
# zhangsan.speak()  # 输出zhangsan会说话

# 创建第二个对象
# lisi = Person()
# print(f"李四:{lisi}")
# lisi.speak()  # 输出李四会说话


# 类中定义属性
# 类属性
# 类属性是属于类本身的属性，定义在“类中，所有方法体外”，所有对象共享同一个属性值，通过类名访问
# 访问方式(1)
'''类名.属性名(推荐)'''
# 访问方式(2)
'''对象名.属性名(不推荐，容易混淆)'''
# 修改方式:只能通过类名.属性名修改
# class Person:
#     # 定义类属性
#     country = "中国"
#     hari_color = "黑色"


# 类名.属性名访问属性
# print(Person.country)  # 输出中国
# print(Person.hari_color)  # 输出黑色
# 对象名.属性名访问属性,不推荐
# p1 = Person()
# p2 = Person()
# print(p1.country)  # 输出中国
# print(p1.hari_color)  # 输出黑色
# print("-----------------")
# 修改类属性
# Person.country = "美国"
# print(f"修改后类属性:{Person.country}")  # 输出美国
# print("-")
# 对象名.属性名修改类属性,不推荐
# p1.country = "日本"  # 新创建p1对象的实例属性，类属性并未修改成功
# 通过对象名.属性名修改类属性，对象属性不会改变，本质上只是新建该对象的实例属性，只影响到p1对象，不影响其他对象
# print(f"修改后类属性:{Person.country}")  # 输出美国
# print(f"修改后通过p1查看属性:{p1.country}")  
# print(f"修改后通过p2查看属性:{p2.country}")


# 实例属性
# 实例属性是类的实例方法中(self.属性)或对象赋值的属性，绑定到具体的对象上，每个对象单独拥有，互不影响
# 访问方式：
'''对象名.属性名'''
# 修改方式：
'''对象名.属性名 = 新值'''
# class Person:
#     # 定义实例方法
#     def say_hello(self):
#         print(f"你好呀!我是{self.name}")
        

# 实例化对象
# p1 = Person()
# p2 = Person()
# p3 = Person()
# p1.say_hello() # 报错，实例属性没有赋值
# 给实例属性赋值
# p1.name = "张三"
# p2.name = "李四"
# p3.name = "赵六"
# # 访问实例属性
# print(p1.name)  # 输出张三
# print(p2.name)  # 输出李四
# 调用实例方法
# p1.say_hello()  # 输出你好呀!我是张三
# p2.say_hello()  # 输出你好呀!我是李四
# 修改p1实例属性
# p1.name = "王五"
# print(p1.name)  # 成功修改为王五
# print(p2.name)  # 没有变化，还是李四
# 实例属性互相独立，互不影响

# 构造方法：__init__()
# 构造方法是类中定义的特殊方法，用于初始化对象的属性，当创建对象时自动调用
# 语法:
'''
class 类名:
    def __init__(self, 参数1, 参数2, ...):
        # 初始化属性
        self.属性1 = 参数1
        self.属性2 = 参数2
        ...
'''

class Person:
    # 定义实例方法
    # def __init__(self):
    #     print(f"你好呀!我是{self.name}，今年{self.age}岁，性别是{self.gender},住在{self.citi}。")
    # 定义构造方法(实例方法)，定义实例属性最佳方式
    def __init__(self, name, age, gender, citi):
        print("我是构造方法，用于初始化对象的属性。")
        self.name = name
        self.age = age
        self.gender = gender
        self.citi = citi
        print(f"你好呀!我是{self.name}，今年{self.age}岁，性别是{self.gender},住在{self.citi}。")

p1 = Person("张三", 20, "男", "北京")  # 创建对象时自动调用,按顺序输入参数，也可以==赋值
p2 = Person("李四", 25, "女", "上海")

# 查看对象属性
print(p1.name)  # 输出张三
print(p1.age)  # 输出20
print(p2.name)  # 输出张三
print(p2.age)  # 输出20
