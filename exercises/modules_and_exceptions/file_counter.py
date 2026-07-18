# 第二题：统计文件中单词总数。
# 写一个函数 count_words_in_file(filepath)，尝试打开指定文件并统计单词总数
# 如果文件不存在，捕获 FileNotFoundError 并返回 None
# 如果文件存在但编码有问题，捕获 UnicodeDecodeError 并返回 None
# 在主程序中调用，传入一个不存在的文件路径，验证异常处理是否生效
def count_words_in_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            return len(content.split())
    except FileNotFoundError:
        print("文件不存在时打印错误")
        return None
    except UnicodeDecodeError:
        print("文件不是文本格式时打印错误")
        return None

if __name__ == "__main__":
    # 测试文件存在的情况
    result1 = count_words_in_file(r"exercises\modules_and_exceptions\test.txt")
    print(f"单词数：{result1}")
    
    # 测试文件不存在的情况
    result2 = count_words_in_file("不存在的文件.txt")
    print(result2)
