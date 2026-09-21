# 此文件用于练习文件编码&文件目录
# 常见的编码有：
# 1. UTF-8：1-3字节 是字符编码支持所有语言，兼容ascii,推荐使用
# 2. GBK：1-2字节 是中文编码兼容gb2312
# 3. ascii:1字节 是英文编码

# with open(r"exercises\file_operations\tast.txt", "+w") as f:   # 不指定encoding默认采用平台编码，Windows平台默认使用gbk编码
    # print(f.write("你好，hllow"))  # 本次输入用gbk编码，文本文件查看用UTF-8，编码不一致会出现乱码

# 目录常用方法
import os
# 1.文件或目录重命名: os.rename
# 同时支持文件/文件夹的移动
# os.rename(r"exercises\file_operations\tast.txt", r"exercises\file_operations\test.txt")
# 注意：源文件或目录的路径必须存在，目标文件或目录路径不能已存在，否则报错
# 不支持跨盘移动


# 2.删除文件路径: or.remove
# 删除指定文件，不能删除文件夹
# os.remove(r"exercises\file_operations\test.txt")  # 删除的文件必须存在，否则报错


# 3.创建单个目录(文件夹): os.mkdir
# os.mkdir("chenyuz")  # 文件夹存在时会报错
# 如果想要创建到指定目录，要写完整路径


# 4.删除目录路径: os.rmdir
# 只能删除空目录，如果文件夹里有文件/子文件夹，抛出OSError: [WinError 145]
# 若文件夹不存在报错抛出FileNotFoundError
# os.rmdir("chenyuz")


# 5.获取绝对路径: os.getcwd()
# 获取当前python程序的 当前工作目录，返回一个绝对路径字符串
# print(os.getcwd())


# 6.列出指定目录下的所有内容: os.listdir()
# 列表中元素包含: 该目录下的所有文件 + 所有文件夹的名称
# print(os.listdir("star_rail_battle"))
# print(os.listdir())  #不指定参数，返回当前目录


# 7.判断指定路径是否存在: os.path.exists()
# 返回一个布尔值，表示路径是否存在
# print(os.path.exists("star_rail_battle"))
# print(os.path.exists("non_existent_directory"))


# 8.判断指定路径 是否为 存在的文件: os.path.isfile()
# 返回一个布尔值，表示路径是否为存在的文件
# print(os.path.isfile("star_rail_battle"))   # 不是文件False
# print(os.path.isfile(r"exercises\file_operations\tast.txt"))
# print(os.path.isfile(r"exercises\file_operations\tast1.txt"))

# 9.判断指定路径 是否为 存在的文件夹: os.path.isdir
print(os.path.isdir("star_rail_battle"))
print(os.path.isdir(r"exercises\file_operations\tast.txt"))
print(os.path.isdir(r"exercises\file_operations\tast1.txt"))