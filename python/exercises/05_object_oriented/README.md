# 05_object_oriented：面向对象编程

本目录覆盖类与对象、封装、继承、多态、类方法 / 静态方法、多重继承与 MRO。
脚本把原来的纯注释笔记补成了「注释讲知识 + 代码给结论」，可以直接运行。

## 文件说明

| 文件 | 对应练习 |
| --- | --- |
| `01_class_basics.py` | 类的定义、对象、实例方法、类属性、实例属性、`__init__`、`__str__`、`__del__` |
| `02_encapsulation.py` | 封装：私有属性、getter / setter、`@property`、名称改写 |
| `03_inheritance.py` | 继承与方法重写、`super()`、私有方法不可被子类访问 |
| `04_polymorphism.py` | 多态（鸭子类型 / 继承 + 重写）、类方法、静态方法、绑定与非绑定方法 |
| `05_static_method_rectangle.py` | 静态方法实战：矩形面积与周长（修正 perimeter 拼写错误） |
| `06_multiple_inheritance_mro.py` | 多重继承、`__mro__`、`super()` 在 MRO 链上的调用顺序 |

## 运行命令

在仓库根目录执行：

```bash
python python/exercises/05_object_oriented/01_class_basics.py
python python/exercises/05_object_oriented/02_encapsulation.py
python python/exercises/05_object_oriented/03_inheritance.py
python python/exercises/05_object_oriented/04_polymorphism.py
python python/exercises/05_object_oriented/05_static_method_rectangle.py
python python/exercises/05_object_oriented/06_multiple_inheritance_mro.py
```
