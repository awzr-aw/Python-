# 06_regex：正则表达式入门

本目录练习 Python 标准库 `re` 模块：常用函数、匹配对象、正则语法规则，
以及贪婪 / 非贪婪、分组、边界等容易踩坑的点。全部脚本用固定文本演示，
可以直接运行、不会阻塞。

## 文件说明

| 文件 | 对应练习 |
| --- | --- |
| `01_re_module_basics.py` | `re.match` / `search` / `findall` / `finditer` / `sub` 的用法与匹配对象的 `group()/start()/end()` |
| `02_grammar_rules.py` | 正则语法规则手册：字符类、量词、分组、贪婪与非贪婪、转义与边界、标志位 |
| `03_grammar_solutions.py` | `02_grammar_rules.py` 中 5 道 TODO 的完整实现与结果对比 |

## 运行命令

在仓库根目录执行（退出码 0 表示运行正常）：

```bash
python python/exercises/06_regex/01_re_module_basics.py
python python/exercises/06_regex/02_grammar_rules.py
python python/exercises/06_regex/03_grammar_solutions.py
```

## 学习建议

先读 `02_grammar_rules.py` 里每小节的「规则」与可运行结论，自己动手把该小节的
TODO 写出来，再和 `03_grammar_solutions.py` 对照。重点不在背语法，而在理解
「贪婪为什么只匹配出一整段」「为什么要加 `\b` / `^$`」这类行为差异。
