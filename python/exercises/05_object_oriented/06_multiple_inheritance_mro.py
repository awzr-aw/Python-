# 06_multiple_inheritance_mro.py
# 【多重继承与 MRO】一个子类可以继承多个父类，方法查找顺序由 __mro__ 决定。
# 来源：原 object_oriented/lnheritance.py 末尾的多重继承部分。
# 运行：python python/exercises/05_object_oriented/06_multiple_inheritance_mro.py
#
# 语法：class 类名(父类名1, 父类名2, ...)
# python 用内置属性 __mro__ 明确方法调用顺序：
#   子类 -> 左侧父类 -> 右侧父类 -> 更上层父类 -> object
#
# 修正说明：原文件里 D.func() 的方法体只有 pass（什么都不做），运行时看不出调用顺序，
#   也留下了「空实现」的坏味道。这里让 D.func() 打印自己的名字并用 super() 继续走 MRO 链。


class A:
    def func(self):
        print("A类的方法")


class B(A):
    def func(self):
        print("B类的方法")
        super().func()          # 沿 MRO 继续找下一个 func


class C(A):
    def func(self):
        print("C类的方法")
        super().func()


class D(B, C):
    def func(self):
        print("D类的方法")
        super().func()


def show_mro_chain():
    print("===== 1. super() 沿 MRO 链依次调用 =====")
    d = D()
    d.func()                     # D -> B -> C -> A
    print("注意：D 的 MRO 是 D, B, C, A，所以 B 里的 super() 会走到 C，而不是直接跳到 A。")


def show_mro_list():
    print("\n===== 2. __mro__ 明确方法查找顺序 =====")
    for cls in D.__mro__:
        print(f"  {cls.__name__}")
    print("顺序：子类 -> 左侧父类 -> 右侧父类 -> 更上层父类 -> object")
    print("C3 线性化保证：每个类只出现一次，且父类一定排在子类之后。")


def show_manual_parent_call():
    print("\n===== 3. 手动指定从某个父类开始调用（非绑定调用）=====")
    d = D()
    print("B.func(d) 的输出：")
    B.func(d)                    # 从 B 开始，super() 仍按 D 的 MRO 走到 C、A
    print("C.func(d) 的输出：")
    C.func(d)                    # 从 C 开始，只走 C、A


def main():
    show_mro_chain()
    show_mro_list()
    show_manual_parent_call()


if __name__ == "__main__":
    main()
