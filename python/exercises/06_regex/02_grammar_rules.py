# 02_grammar_rules.py
# 【正则语法规则】字符类 / 量词 / 分组 / 贪婪与非贪婪 / 转义与边界。
# 来源：原 regex/syntax_rules.py 是 0 字节空文件，这里补成可直接运行的规则手册。
# 每个小节先给结论（print 出来的真实匹配结果），末尾留一道 TODO 练习题，
# 对应的参考答案在同目录 03_grammar_solutions.py。
# 运行：python python/exercises/06_regex/02_grammar_rules.py

import re

PHONE_RULE = r"^1\d{10}$"   # 11 位手机号：1 开头，后面 10 个数字


# ==================== 1. 字符类 ====================
def demo_character_classes():
    r"""字符类：用 [] 表示「其中任意一个字符」，\d \w \s 是预定义的字符类。"""
    print("===== 1. 字符类 =====")
    print(r"规则：[abc] 匹配 a/b/c 任意一个；[^abc] 取反；[a-z] 范围；")
    print(r"      \d 数字；\D 非数字；\w 字母数字下划线；\W 取反；\s 空白；\S 取反；. 除换行外任意字符")
    print(f"re.findall(r'[abc]', 'a1b2c3')     -> {re.findall(r'[abc]', 'a1b2c3')}")
    print(f"re.findall(r'[^abc]', 'a1b2c3')    -> {re.findall(r'[^abc]', 'a1b2c3')}")
    print(f"re.findall(r'[aeiou]', 'hello')    -> {re.findall(r'[aeiou]', 'hello')}")
    print(f"re.findall(r'\\d', 'a1b2c3')        -> {re.findall(r'\d', 'a1b2c3')}")
    print(f"re.findall(r'\\w+', 'hi there_1')   -> {re.findall(r'\w+', 'hi there_1')}")
    print(f"re.findall(r'\\s', 'a b\\tc')       -> {re.findall(r'\s', 'a b\tc')}")
    print("TODO：从 '2026-10-09' 里用字符类取出年、月、日三个数字。")


# ==================== 2. 量词 ====================
def demo_quantifiers():
    """量词：控制它前面那个字符 / 分组重复出现的次数。"""
    print("\n===== 2. 量词 =====")
    print(r"规则：* 0 次或多次；+ 1 次或多次；? 0 次或 1 次；")
    print(r"      {m} 恰好 m 次；{m,} 至少 m 次；{m,n} m 到 n 次")
    print(f"re.findall(r'a+', 'a aa aaa b')     -> {re.findall(r'a+', 'a aa aaa b')}")
    print(f"re.findall(r'ab?c', 'ac abc abbc')  -> {re.findall(r'ab?c', 'ac abc abbc')}")
    print(f"re.findall(r'\\d{4}', '2026-10-09')  -> {re.findall(r'\d{4}', '2026-10-09')}")
    print(f"re.findall(r'\\d{2,3}', '1 12 123 1234') -> {re.findall(r'\d{2,3}', '1 12 123 1234')}")
    print("注意：量词默认贪婪——`\\d{2,3}` 会优先一次吃 3 个数字。")
    print("TODO：用 {m,n} 匹配 3~4 位数字，测试 '12 123 1234 12345'。")


# ==================== 3. 分组 ====================
def demo_groups():
    """分组：() 把一段规则打包，匹配后可以单独取出各部分。"""
    print("\n===== 3. 分组 =====")
    date_rule = r"(\d{4})-(\d{2})-(\d{2})"
    print(f"re.findall(r'{date_rule}', '日期 2026-10-09') -> "
          f"{re.findall(date_rule, '日期 2026-10-09')}   # 有分组时返回元组")
    match = re.search(date_rule, "日期 2026-10-09")
    print(f"search + group(0/1/2/3) -> {match.group(0)} / {match.group(1)} / "
          f"{match.group(2)} / {match.group(3)}")
    named = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})", "2026-10")
    print(f"命名分组 group('year') / groupdict() -> {named.group('year')} / {named.groupdict()}")
    print(f"非捕获分组 re.findall(r'(?:ab)+', 'ababab') -> {re.findall(r'(?:ab)+', 'ababab')}")
    print("经验：只做整体匹配、不需要单独取值的部分用 (?:...) 非捕获分组，结果更干净。")
    print("TODO：从 '编号:101 姓名:张三' 里分别取出编号和姓名。")


# ==================== 4. 贪婪与非贪婪 ====================
def demo_greedy_lazy():
    """贪婪与非贪婪：量词默认尽可能多，加 ? 后尽可能少。"""
    print("\n===== 4. 贪婪与非贪婪 =====")
    text = "<b>标题</b><i>正文</i>"
    print(f"原串：{text}")
    print(f"贪婪   re.findall(r'<.+>', text)  -> {re.findall(r'<.+>', text)}")
    print(f"非贪婪 re.findall(r'<.+?>', text) -> {re.findall(r'<.+?>', text)}")
    print("原因：贪婪的 `.+` 先一路吃到行尾再回退，所以只留一个最长匹配；")
    print("      `.+?` 每吃一个字符就尝试结束，于是每个标签各匹配一次。")
    print("TODO：解释为什么贪婪模式只匹配出一整段，而不是每个标签各一段。")


# ==================== 5. 转义与边界 ====================
def demo_escape_and_boundary():
    """转义与边界：元字符要转义；^ $ \\b 表示位置而不是字符。"""
    print("\n===== 5. 转义与边界 =====")
    print("元字符（要匹配本身必须加反斜杠）：. ^ $ * + ? { } [ ] \\ | ( )")
    print(f"re.findall(r'\\d+\\.\\d+', '3.14 和 2.71') -> {re.findall(r'\d+\.\d+', '3.14 和 2.71')}")
    print(f"re.findall(r'\\bcat\\b', 'cat category cat') -> {re.findall(r'\bcat\b', 'cat category cat')}")
    print(f"re.match(r'^\\d+$', '12345')  -> {bool(re.match(r'^\d+$', '12345'))}")
    print(f"re.match(r'^\\d+$', '12a45')  -> {bool(re.match(r'^\d+$', '12a45'))}")
    print(f"re.findall(r'^\\w+', 'hello world', re.MULTILINE) -> "
          f"{re.findall(r'^\w+', 'hello world', re.MULTILINE)}")
    print("常用标志位：re.I 忽略大小写、re.M 多行、re.S 让 . 匹配换行、re.X 允许注释空格")
    print(f"re.findall('python', 'Python PYTHON', re.I) -> {re.findall('python', 'Python PYTHON', re.I)}")
    print("TODO：用正则校验 11 位手机号（1 开头），输出 True / False。")


# ==================== TODO 参考答案入口 ====================
def check_phone(number):
    """TODO 的参考实现：11 位手机号校验，返回 True / False。"""
    return re.match(PHONE_RULE, number) is not None


def main():
    demo_character_classes()
    demo_quantifiers()
    demo_groups()
    demo_greedy_lazy()
    demo_escape_and_boundary()
    print("\n===== TODO 自测（参考答案见 03_grammar_solutions.py）=====")
    for number in ("13812345678", "1381234567", "23812345678"):
        print(f"  check_phone({number!r}) -> {check_phone(number)}")
    print("\n全部小节运行完毕；把每节末尾的 TODO 换成自己的实现再来对比答案。")


if __name__ == "__main__":
    main()
