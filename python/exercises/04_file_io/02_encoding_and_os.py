# 02_encoding_and_os.py
# 【文件编码 & os 目录操作】GBK / UTF-8 读取差异，以及 os.path 常用判断。
# 来源：原 file_operations/file_encoding.py。
# 运行：python python/exercises/04_file_io/02_encoding_and_os.py
#
# 常见编码（保留原笔记）：
#   UTF-8：1~3 字节，支持所有语言，兼容 ASCII，推荐使用；
#   GBK：1~2 字节，中文编码，兼容 GB2312；
#   ASCII：1 字节，只能表示英文。
# 注意：同一个文件用错编码去读，要么乱码，要么直接抛 UnicodeDecodeError。
# data/sample_gbk.txt 是故意保留的 GBK 样例，原始字节为
#   C4 E3 BA C3 A3 AC 68 6C 6C 6F 77  （即"你好，hllow"）
#
# 修正说明：原文件末尾用相对路径直接 print(os.path.isdir(...))，跑出来的结果取决于
#   当前工作目录，而且会真的去改磁盘（os.rename / os.remove）。这里路径全部基于 __file__，
#   真正会改动磁盘的操作只作用在脚本目录的临时演示文件上，用完立即删除。
#   （不使用 tempfile：本机沙箱下程序自己新建的临时目录可能拿不到写权限。）

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
UTF8_FILE = os.path.join(DATA_DIR, "sample_utf8.txt")
GBK_FILE = os.path.join(DATA_DIR, "sample_gbk.txt")
# 文件操作的临时演示文件；带进程号避免并发运行互相干扰，用完在 finally 里删除
DEMO_FILE = os.path.join(BASE_DIR, f"_encoding_demo_{os.getpid()}.txt")


def show_encoding():
    """同一个 GBK 文件：用 gbk 读成功，用 utf-8 读抛 UnicodeDecodeError。"""
    with open(GBK_FILE, "r", encoding="gbk") as file:
        content = file.read()
    print(f"用 gbk 读取 sample_gbk.txt：{content!r}")

    try:
        with open(GBK_FILE, "r", encoding="utf-8") as file:
            file.read()
    except UnicodeDecodeError as error:
        print(f"用 utf-8 读取同一个文件：UnicodeDecodeError -> {error}")

    with open(UTF8_FILE, "r", encoding="utf-8") as file:
        print(f"用 utf-8 读取 sample_utf8.txt：{file.read()!r}")


def show_os_path():
    """路径判断与拼接：全部基于 __file__，换工作目录也不会错。"""
    print(f"os.getcwd()（当前工作目录）：{os.getcwd()}")
    print(f"脚本所在目录：{BASE_DIR}")
    print(f"data 目录内容：{sorted(os.listdir(DATA_DIR))}")
    print(f"os.path.exists(DATA_DIR) -> {os.path.exists(DATA_DIR)}")
    print(f"os.path.exists('不存在的目录') -> {os.path.exists('不存在的目录')}")
    print(f"os.path.isfile(UTF8_FILE) -> {os.path.isfile(UTF8_FILE)}")
    print(f"os.path.isdir(DATA_DIR) -> {os.path.isdir(DATA_DIR)}")
    print(f"os.path.isdir(UTF8_FILE) -> {os.path.isdir(UTF8_FILE)}")
    print(f"os.path.basename(UTF8_FILE) -> {os.path.basename(UTF8_FILE)}")
    print(f"os.path.join('a', 'b', 'c.txt') -> {os.path.join('a', 'b', 'c.txt')}")


def show_os_file_operations():
    """会改动磁盘的 os 操作：只作用在脚本目录的临时演示文件上，用完一定删除。"""
    renamed = DEMO_FILE + ".bak"
    try:
        with open(DEMO_FILE, "w", encoding="utf-8") as file:
            file.write("临时文件")
        print(f"创建演示文件成功：{os.path.exists(DEMO_FILE)}")

        os.rename(DEMO_FILE, renamed)          # 重命名（也可用于移动，不能跨盘）
        print(f"os.rename 后 .bak 存在：{os.path.exists(renamed)}")
        print(f"os.rename 后原文件存在：{os.path.exists(DEMO_FILE)}")

        os.remove(renamed)                     # 删除文件（不能删目录）
        print(f"os.remove 后 .bak 存在：{os.path.exists(renamed)}")
    finally:
        for path in (DEMO_FILE, renamed):
            if os.path.exists(path):
                os.remove(path)
                print(f"已清理临时文件：{os.path.basename(path)}")


def show_os_dir_errors():
    """目录操作的规则用失败路径演示，不真的改动磁盘也能看到结论。"""
    try:
        os.mkdir(DATA_DIR)                     # 目录已存在时会报错
        print("os.mkdir 意外成功了")
    except FileExistsError as error:
        print(f"os.mkdir 一个已存在的目录 -> FileExistsError：{error}")

    try:
        os.rmdir(DATA_DIR)                     # 只能删除空目录
        print("os.rmdir 意外成功了")
    except OSError as error:
        print(f"os.rmdir 一个非空目录 -> OSError：{error}")


def main():
    print("===== 1. 编码差异 =====")
    show_encoding()
    print("\n===== 2. os.path 路径操作 =====")
    show_os_path()
    print("\n===== 3. os 的文件改名 / 删除（脚本目录临时文件演示）=====")
    show_os_file_operations()
    print("\n===== 4. os 目录操作的报错规则（失败路径演示）=====")
    show_os_dir_errors()


if __name__ == "__main__":
    main()
