# 03_grammar_solutions.py
# 【正则语法规则·参考答案】02_grammar_rules.py 里 5 道 TODO 的完整实现。
# 每题：先写题面，再给函数实现，最后用固定数据跑出结果（不依赖 input()）。
# 运行：python python/exercises/06_regex/03_grammar_solutions.py

import re

# ==================== 题目 1：字符类 ====================
# 从 '2026-10-09' 里用字符类取出年、月、日三个数字。
DATE_TEXT = "2026-10-09"


def split_date(text):
    """返回 (年, 月, 日)。用捕获分组一次性取出三段数字。"""
    match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
    if match is None:
        return None
    year, month, day = match.groups()
    return year, month, day


def split_date_digits(text):
    """另一种写法：只匹配数字后再切片，演示 findall 的结果。"""
    numbers = re.findall(r"\d+", text)
    return (numbers[0], numbers[1], numbers[2]) if len(numbers) >= 3 else None


# ==================== 题目 2：量词 ====================
# 用 {m,n} 匹配 3~4 位数字，测试 '12 123 1234 12345'。
NUMBER_TEXT = "12 123 1234 12345"


def find_3_to_4_digits(text):
    """返回所有 3~4 位数字。注意贪婪：12345 会被切成 1234 与剩余部分。"""
    return re.findall(r"\d{3,4}", text)


def find_whole_3_to_4_digits(text):
    """加上单词边界，只取独立的 3~4 位数字，避免从长数字中间截断。"""
    return re.findall(r"\b\d{3,4}\b", text)


# ==================== 题目 3：分组 ====================
# 从 '编号:101 姓名:张三' 里分别取出编号和姓名。
STUDENT_TEXT = "编号:101 姓名:张三"


def parse_student(text):
    """返回 {'编号': ..., '姓名': ...}，用命名分组提高可读性。"""
    match = re.search(r"编号:(?P<id>\d+)\s+姓名:(?P<name>\S+)", text)
    return match.groupdict() if match else None


# ==================== 题目 4：贪婪 / 非贪婪 ====================
# 为什么贪婪模式只匹配出一整段，而不是每个标签各一段？
GREEDY_TEXT = "<b>标题</b><i>正文</i>"


def explain_greedy():
    """给出可验证的对比结论。"""
    greedy = re.findall(r"<.+>", GREEDY_TEXT)
    lazy = re.findall(r"<.+?>", GREEDY_TEXT)
    return greedy, lazy


# ==================== 题目 5：转义与边界 ====================
# 用正则校验 11 位手机号（1 开头），输出 True / False。
PHONE_RULE = re.compile(r"^1\d{10}$")


def is_phone(number):
    """1 开头、共 11 位数字；用 fullmatch 更直观（相当于 ^...$）。"""
    return PHONE_RULE.fullmatch(number) is not None


def main():
    print("===== 参考答案 1：字符类 =====")
    print(f"split_date({DATE_TEXT!r})        -> {split_date(DATE_TEXT)}")
    print(f"split_date_digits({DATE_TEXT!r}) -> {split_date_digits(DATE_TEXT)}")

    print("\n===== 参考答案 2：量词 =====")
    print(f"re.findall(r'\\d{{3,4}}', {NUMBER_TEXT!r})   -> {find_3_to_4_digits(NUMBER_TEXT)}")
    print(f"re.findall(r'\\b\\d{{3,4}}\\b', {NUMBER_TEXT!r}) -> {find_whole_3_to_4_digits(NUMBER_TEXT)}")
    print("结论：不加 \\b 时，12345 会被贪婪地切成 1234；加边界后只剩独立的 123 和 1234。")

    print("\n===== 参考答案 3：分组 =====")
    print(f"parse_student({STUDENT_TEXT!r}) -> {parse_student(STUDENT_TEXT)}")

    print("\n===== 参考答案 4：贪婪 / 非贪婪 =====")
    greedy, lazy = explain_greedy()
    print(f"贪婪   re.findall(r'<.+>', text)  -> {greedy}")
    print(f"非贪婪 re.findall(r'<.+?>', text) -> {lazy}")
    print("结论：贪婪的 .+ 会先吃到最后一个 >，因此只产生 1 个最长匹配；")
    print("      非贪婪的 .+? 每步都尝试结束，于是每个标签各匹配 1 次。")

    print("\n===== 参考答案 5：转义与边界 =====")
    for number in ("13812345678", "1381234567", "23812345678", "1381234567a"):
        print(f"is_phone({number!r}) -> {is_phone(number)}")
    print("结论：^ 与 $ 保证整串匹配；写成 re.search 而漏掉两端锚点会误判超长号码。")

    print("\n全部参考答案运行完毕。")


if __name__ == "__main__":
    main()
