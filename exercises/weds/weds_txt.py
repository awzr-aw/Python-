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

with open(r'exercises\weds\weds.txt', 'r') as f:
    print(f.name)
    print(f.mode)
    print(f.closed) # 有缩进的代码为代码块,未执行完代码文件不会关闭
# 代码块全部执行结束,才会自动调用close()函数
print("执行关闭文件操作后....")
print(f.closed) # 未执行完代码文件不会关闭