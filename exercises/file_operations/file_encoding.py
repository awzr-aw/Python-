# 此文件用于练习文件编码&文件目录
# 常见的编码有：
# 1. UTF-8：1-3字节 是字符编码支持所有语言，兼容ascii,推荐使用
# 2. GBK：1-2字节 是中文编码兼容gb2312
# 3. ascii:1字节 是英文编码

with open(r"exercises\file_operations\tast.txt", "+w") as f:   # 不指定encoding默认采用平台编码，Windows平台默认使用gbk编码
    print(f.write("你好，hllow"))  # 本次输入用gbk编码，文本文件查看用UTF-8，编码不一致会出现乱码

# 目录常用方法
import os
# 1.文件或目录重命名: os.rename
# 同时支持文件/文件夹的移动
os.rename(r"exercises\file_operations\tast.txt", r"exercises\file_operations\test.txt")