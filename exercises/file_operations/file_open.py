# 文件的打开关闭&读写文件内容
# 打开文件
# open(文件路径, 访问模式='r', encoding=None)
# 文件路径：文件的路径，可以是绝对路径或相对路径，必须要有
# 访问模式：访问模式有以下几种：
# 'r'：只读模式，只能读取文件内容，不能写入文件内容
# 'w'：写入模式，如果文件不存在，则创建文件，如果文件存在，则清空文件内容
# 'a'：追加模式，在文件末尾追加内容，如果文件不存在，则创建文件
# 'r+':读写模式，可以读取和写入文件内容
# 'w+':读写模式，如果文件不存在，则创建文件，如果文件存在，则清空文件内容
# 'a+':读写模式，写入时只能追加到末尾，读取时可读取全部内容，文件不存在时创建
# encoding:仅在文本模式有效，指定文件的编码格式，默认使用系统编码

# 二进制模式：在文本访问模式后面添加'b'(如'rb''wb'),用于处理二进制(图片，音频等)
# 操作的是字节数据(bytes类型)，此时不需要指定encoding参数
# 文件对象常见属性
# name：文件名
# mode：访问模式
# encoding：编码格式
# closed：文件是否关闭
# f = open(r'exercises\weds\weds.txt', 'r')
# print(f.name)
# print(f.mode)
# print(f.encoding)


# 相对路径：相对当前程序所在目录的路径，不包含完整的根路径信息
# 层级关系：一个.表示当前目录(可省略)，..表示上一级目录
# 绝对路径：包含完整的根路径信息，如C:\Users\19990\Desktop\git\exercises\weds\weds.txt
# 当前程序所在目录：程序运行时所在的目录，可以通过os模块获取

# 关闭文件
# 1.close()：手动关闭文件
# print(f.closed)
# f.close()
# print("执行关闭文件操作后....")
# print(f.closed)
# 2.使用with语句：自动关闭文件，不需要手动关闭
'''with open(文件路径, 访问模式='r', encoding=None) as 文件对象：
    文件对象的操作
with语句会自动调用文件对象的close()方法，关闭文件'''

# with open(r'exercises\weds\weds.txt', 'r') as f:
#     print(f.name)
#     print(f.mode)
#     print(f.closed) # 有缩进的代码为代码块,未执行完代码文件不会关闭
# # 代码块全部执行结束,才会自动调用close()函数
# print("执行关闭文件操作后....")
# print(f.closed) # 未执行完代码文件不会关闭

# 读取文件
# 1.读取文件内容
# read(size)：读取文件所有内容，返回字符串,文本模式下返回指定读取的size字符数
# 二进制模式则返回指定读取的size字节，默认读取全部内容
# with open(r'exercises\weds\weds.txt', 'r', encoding="utf-8") as f:
#     # print(f.read())
#     print(f.read(10)) # 读取10个字符
#     print(f.read(10)) # 读取10个字符
#     print(f.read(10)) # 多次使用read()不会从头读取，会在上个读取位置继续读取

# read方法在读取非常大的文件时，会一次性加载到内存中，会给系统带来压力，推荐在较小的文件中使用

# 2.逐行读取文件内容
# readline(size)：读取文件的下一行内容，返回字符串,文本模式下返回指定读取的size字符数
# with open(r'exercises\weds\weds.txt', 'r', encoding="utf-8") as f:
#     print(f.readline().strip()) # strip()去除换行符
#     print(f.readline().strip()) # 会读取换行符，多次使用readline()不会从头读取，会在上个读取行继续读取
#     print(f.readline()) # 如果行数不够不会报错

# 3.读取所有行
# readlines()：读取所有行内容，返回列表，列表中的每个元素为一行内容(包括换行符)
# with open(r'exercises\weds\weds.txt', 'r', encoding="utf-8") as f:
#     print(f.readlines()) # 对大文件不推荐

# for循环遍历,适合处理大文件
# with open(r'exercises\weds\weds.txt', 'r', encoding="utf-8") as f:
#     for line in f:
#         print(line.strip()) # strip()去除换行符

# 写入文件
# 1.写入文件内容
# write(str)：写入字符串内容或字节数据，文本模式下写入的是字符串，二进制模式下写入的是字节
# 特点：不会自动换行，需要手动添加换行符
# 如果'w'模式打开文件，写入前会清空原有内容；如果'a'模式打开文件，写入内容会追加到文件末尾
# w: 写入模式，如果文件不存在，则创建文件，如果文件存在，则清空文件内容
# with open(r'exercises\weds\weds.txt', 'w', encoding="utf-8") as f:
#     f.write("Hello, World!\n") # 写入字符串,会清空文件内容

# a: 追加模式，在文件末尾追加内容，如果文件不存在，则创建文件
# with open(r'exercises\weds\weds.txt', 'a', encoding="utf-8") as f:
# with open(r"exercises\weds\tast.txt", 'a', encoding="utf-8") as f:
#     f.write("Hello, World!\n") # 追加内容

# +: 读写模式，可以与r,w,a模式结合使用,实现对文件读写

# with open(r'exercises\weds\weds.txt', 'w+', encoding="utf-8") as f:
#     print(f.write("这是第一行\n"))
#     print(f.write("这是第二行\n")) # 写入文件内容时，指针会停留在文件末尾
#     # 文件指针当前位置决定了下一次文件操作从哪开始
#     print(f.seek(0)) # 移动文件指针到文件开头

#     print(f.read()) # 如果不写seek()，则从文件末尾开始读取，内容为空

# 文件定位操作
# tell():返回文件指针当前位置
# seek(偏移量, 参考点=0)：移动文件指针到指定位置
# seek(0): 移动文件指针到文件开头
# with open(r'exercises\weds\weds.txt', 'w+', encoding="utf-8") as f:
#     f.write("aaa\n") # \n替换为-->\r\n
#     f.write("bbb\n")
#     f.write("ccc\n")
#     # 移动前文件指针位置
#     print(f.tell()) # 15
#     # 移动后文件指针位置
#     f.seek(0)
#     print(f.tell()) # 0
#     print(f.read())
#     f.seek(10)


# 2.可迭代写入对象
# writerlines():用于批量写入多行内容，接受一个可迭代的字符串序列(如列表，元组，生成器等)作为参数
# lines = ["aaa\n", "bbb\n", "ccc\n", "ddd\n"]
# with open(r'exercises\weds\weds.txt', 'w+', encoding="utf-8") as f:
#     f.writelines(lines) # 批量写入多行内容

'''以上内容在没有更改文件名时写的，如果要运行请更改路径'''