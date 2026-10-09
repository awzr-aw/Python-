# 01_file_read_write.py
# 【文件读写】open() 的访问模式、文件对象属性、读 / 写 / 指针定位操作。
# 来源：原 file_operations/file_open.py（原来整篇都是注释，跑不出结果，这里补上可运行演示）。
# 运行：python python/exercises/04_file_io/01_file_read_write.py
#
# 知识速查（保留原笔记）：
#   open(文件路径, 访问模式='r', encoding=None)
#     'r'  只读，文件不存在报错        'w'  只写，不存在则创建，存在则清空
#     'a'  追加，不存在则创建          'r+' 读写，文件必须存在
#     'w+' 读写，存在则清空            'a+' 读写，写入只能追加到末尾
#     'b'  二进制模式（'rb'/'wb'），操作 bytes，不能指定 encoding
#   文件对象属性：name / mode / encoding / closed
#   关闭文件：f.close() 或 with 语句（自动关闭）
#   读取：read(size) / readline() / readlines() / for line in f
#   写入：write(str) / writelines(可迭代对象)
#   定位：tell() 返回指针位置；seek(偏移量[, 参考点]) 移动指针
#
# 修正说明：原文件的路径写成 r'exercises\weds\weds.txt'（改过目录名后已失效），
#   这里用 __file__ 定位同目录的 data/sample_utf8.txt；写操作在脚本目录的临时演示文件里做，
#   运行结束立即删除，不会破坏仓库里的样例数据。
#   （不使用 tempfile：本机沙箱下程序自己新建的临时目录可能拿不到写权限。）

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "sample_utf8.txt")
# 写入演示用的临时文件；带进程号避免并发运行互相干扰，用完在 finally 里删除
DEMO_FILE = os.path.join(BASE_DIR, f"_file_read_write_demo_{os.getpid()}.txt")


def show_file_object():
    """文件对象的常见属性，以及 with 语句如何自动关闭文件。"""
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        print(f"name={file.name}")
        print(f"mode={file.mode}")
        print(f"encoding={file.encoding}")
        print(f"with 代码块内 closed={file.closed}")
    print(f"退出 with 代码块后 closed={file.closed}   # 自动调用了 close()")


def read_back(path, label):
    """重新以只读方式打开并打印内容，用于验证写入结果。"""
    with open(path, "r", encoding="utf-8") as file:
        print(f"{label}内容：{file.read()!r}")


def show_read_methods():
    """read 接着上次位置继续读；readline 每次一行；readlines 一次读成列表。"""
    print("read 是“接着上次位置继续读”：")
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        print(f"  read(3)  -> {file.read(3)!r}")
        print(f"  再 read(3) -> {file.read(3)!r}   # 不会从头开始")

    print("readline 逐行读取：")
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        print(f"  readline() -> {file.readline().strip()!r}")
        print(f"  readline() -> {file.readline().strip()!r}")

    print("readlines 一次读成列表：")
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        print(f"  readlines() -> {file.readlines()}")

    print("for 循环逐行读取（大文件推荐）：")
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        for line in file:
            print(f"  {line.strip()}")

    print("二进制模式读取（返回 bytes，不指定 encoding）：")
    with open(DATA_FILE, "rb") as file:
        print(f"  read(6) -> {file.read(6)!r}")


def show_write_modes():
    """在脚本目录的临时演示文件上演示写入、追加、清空与指针定位，结束前删除它。"""
    try:
        # 'w'：不存在则创建，存在则清空
        with open(DEMO_FILE, "w", encoding="utf-8") as file:
            file.write("第一行\n")   # write 不会自动补换行，需要自己写 \n
            file.write("第二行\n")
        read_back(DEMO_FILE, "'w' 写入后")

        # 'a'：追加到末尾
        with open(DEMO_FILE, "a", encoding="utf-8") as file:
            file.write("第三行（追加）\n")
        read_back(DEMO_FILE, "'a' 追加后")

        # 'w' 再次打开会清空原有内容
        with open(DEMO_FILE, "w", encoding="utf-8") as file:
            file.write("")           # 打开时文件已经被截断为空
        read_back(DEMO_FILE, "'w' 再次打开（未写入）")

        # writelines + seek
        lines = ["aaa\n", "bbb\n", "ccc\n"]
        with open(DEMO_FILE, "w+", encoding="utf-8") as file:
            file.writelines(lines)   # 批量写入多行
            file.seek(0)             # 指针回到开头才能读到内容
            print(f"writelines 后 seek(0) 读全部：{file.read()!r}")

        # tell / seek
        with open(DEMO_FILE, "w+", encoding="utf-8") as file:
            file.write("aaa\n")
            file.write("bbb\n")
            print(f"写入两行后 tell() = {file.tell()}（指针停在末尾）")
            file.seek(0)
            print(f"seek(0) 后 tell() = {file.tell()}，第一行 = {file.readline().strip()!r}")
    finally:
        if os.path.exists(DEMO_FILE):
            os.remove(DEMO_FILE)
            print(f"演示结束，临时文件已删除：{os.path.basename(DEMO_FILE)}")


def main():
    print("===== 1. 文件对象属性与 with 自动关闭 =====")
    show_file_object()
    print("\n===== 2. 读取文件的几种方式 =====")
    show_read_methods()
    print("\n===== 3. 写入、追加与指针定位（临时文件演示）=====")
    show_write_modes()


if __name__ == "__main__":
    main()
