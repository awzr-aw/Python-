# 03_word_counter.py
# 【异常处理 + 路径】统计文件中的单词总数。
# 来源：原 modules_and_exceptions/file_counter.py（数据文件 test.txt -> data/sample_text.txt）。
# 运行：python python/exercises/03_modules_and_exceptions/03_word_counter.py
#
# 原题需求：
#   写一个函数 count_words_in_file(filepath)，尝试打开指定文件并统计单词总数。
#   1) 文件不存在 -> 捕获 FileNotFoundError 并返回 None；
#   2) 文件存在但编码有问题 -> 捕获 UnicodeDecodeError 并返回 None。
#   在主程序中调用，传入一个不存在的文件路径，验证异常处理是否生效。
#
# 修正说明：原代码用的是相对路径 "exercises\\modules_and_exceptions\\test.txt"，
#   换一个工作目录就找不到文件。这里改为基于 __file__ 定位同目录的 data/sample_text.txt，
#   因此在任何工作目录下运行都正确；编码错误的样例直接复用 04_file_io 下保留的 GBK 文件，
#   不再临时创建文件（本机沙箱下程序自己新建的目录可能拿不到写权限）。

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "sample_text.txt")
# 上级目录下的 04_file_io/data/sample_gbk.txt 是故意保留的 GBK 样例
GBK_SAMPLE = os.path.join(os.path.dirname(BASE_DIR), "04_file_io", "data", "sample_gbk.txt")


def count_words_in_file(filepath, encoding="utf-8"):
    """返回文件中的单词数；文件不存在或编码错误时返回 None。"""
    try:
        with open(filepath, "r", encoding=encoding) as file:
            content = file.read()
    except FileNotFoundError:
        print(f"文件不存在：{filepath}")
        return None
    except UnicodeDecodeError:
        print(f"文件无法用 {encoding} 解码：{filepath}")
        return None
    return len(content.split())


def main():
    print("===== 场景1：文件存在，正常统计 =====")
    print(f"文件：{DATA_FILE}")
    print(f"单词数：{count_words_in_file(DATA_FILE)}")

    print("\n===== 场景2：文件不存在（捕获 FileNotFoundError）=====")
    print(f"返回值：{count_words_in_file('不存在的文件.txt')}")

    print("\n===== 场景3：编码不匹配（GBK 字节用 utf-8 读，捕获 UnicodeDecodeError）=====")
    # 直接复用 04_file_io 下故意保留的 GBK 样例，不需要临时造文件
    print(f"文件：{GBK_SAMPLE}")
    print(f"返回值：{count_words_in_file(GBK_SAMPLE)}")


if __name__ == "__main__":
    main()
