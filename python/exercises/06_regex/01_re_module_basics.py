# 01_re_module_basics.py
# 【正则入门】re 模块常用函数与匹配对象的方法。
# 来源：原 regex/meaning.py（保留原有中文笔记，并补上可运行的输出说明）。
# 运行：python python/exercises/06_regex/01_re_module_basics.py
#
# 正则表达式：用「规则字符串」表达对文本的一种匹配逻辑，
# 从而实现对目标字符串的查找、提取、替换。
# 匹配对象常用方法：
#   .group()  获取匹配到的字符串
#   .start()  获取匹配的起始位置（下标从 0 开始）
#   .end()    获取匹配的结束位置（不包含该下标）

import re

TEXT = "hello world, hello python"


def show_match():
    print("===== 1. re.match：从字符串起始位置开始匹配 =====")
    result = re.match("h", "hello")
    print(f"re.match('h', 'hello') -> {result}")
    print(f"group()={result.group()}  start()={result.start()}  end()={result.end()}")
    print(f"match 只在开头找：re.match('l', 'hello') -> {re.match('l', 'hello')}   # None")


def show_search():
    print("\n===== 2. re.search：在整串里查找第一个匹配项 =====")
    result = re.search("l", "hello")
    print(f"re.search('l', 'hello') -> {result}")
    print(f"group()={result.group()}  start()={result.start()}  end()={result.end()}")


def show_findall():
    print("\n===== 3. re.findall：找出所有匹配项，返回列表 =====")
    print(f"re.findall('l', 'hello') -> {re.findall('l', 'hello')}")
    print(f"re.findall('hello', TEXT) -> {re.findall('hello', TEXT)}")


def show_finditer():
    print("\n===== 4. re.finditer：返回迭代器，可以逐个拿到匹配及其位置 =====")
    for match in re.finditer("l", "hello"):
        print(f"  匹配到 {match.group()!r}，位置 [{match.start()}, {match.end()})")


def show_sub():
    print("\n===== 5. re.sub：替换匹配到的内容 =====")
    print(f"re.sub('l', 'L', 'hello') -> {re.sub('l', 'L', 'hello')}")
    print(f"count=1 只替换第一处 -> {re.sub('l', 'L', 'hello', count=1)}")


def main():
    show_match()
    show_search()
    show_findall()
    show_finditer()
    show_sub()
    print("\n小结：match 从开头匹配；search 找第一处；findall 找全部；"
          "finditer 带位置；sub 做替换。")


if __name__ == "__main__":
    main()
