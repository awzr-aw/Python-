# 功能：读取 scores.txt，解析每行数据，返回学生列表。
# 文件读取模块，提供 read_scores 函数
def read_scores(filename):
    students = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) != 4:
                    continue  # 跳过格式不正确的行
                name = parts[0].strip()
                chinese = int(parts[1].strip())
                math = int(parts[2].strip())
                english = int(parts[3].strip())
                student = {
                    "name": name,
                    "scores": {
                        "语文": chinese,
                        "数学": math,
                        "英语": english
                    }
                }
                students.append(student)
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
    except Exception as e:
        print(f"读取文件时出错: {e}")
    return students


if __name__ == "__main__":
    # 测试读取功能（请根据实际路径调整）
    test_path = r"C:\Users\19990\Desktop\git\exercises\student_system\scores.txt"
    students = read_scores(test_path)
    for s in students:
        print(s)
