# 功能：读取 data/scores.txt 成绩文件，解析每行数据，返回学生列表。
# 文件读取模块，提供 read_scores 函数
import os

# 数据文件绝对路径：基于本文件所在目录动态拼接，不再硬编码绝对路径
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "scores.txt")


def read_scores(filename=DATA_FILE):
    """读取成绩文件，返回学生列表：[{"name": 姓名, "scores": {科目: 分数}}, ...]"""
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
    # 测试读取功能：默认读取本目录下 data/scores.txt
    for stu in read_scores():
        print(stu)
