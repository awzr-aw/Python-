# 04_data_structures.py
# Python 基础第二篇：列表、元组、字典、集合的常用操作。
# 来源：原 basics/basics.py 里只写了标题、没有实际内容，这里补齐可运行示例。
# 运行：python python/exercises/01_basics/04_data_structures.py


# ---------- 列表 list：有序、可变、允许重复 ----------
def show_list():
    weights = [70, 65, 80, 68, 72]
    print("原始列表：", weights)
    print("末尾追加 66（原列表不变）：", weights + [66])
    print("切片 [1:4]：", weights[1:4])
    print("切片逆序 [::-1]：", weights[::-1])
    print("最大值/最小值/求和：", max(weights), min(weights), sum(weights))
    print("升序排序：", sorted(weights))
    print("列表推导式（每个体重 -1）：", [w - 1 for w in weights])

    weights.append(66)            # append 才会真的修改原列表
    print("append(66) 后：", weights)


# ---------- 元组 tuple：有序、不可变 ----------
def show_tuple():
    point = (3, 5)
    x, y = point                  # 元组解包
    print(f"元组 {point} 解包后：x={x}, y={y}")
    single = (1,)                 # 单元素元组必须带逗号，否则只是数字 1
    print(f"单元素元组 {single} 的类型：{type(single).__name__}")
    print("元组不可变，适合存放不会修改的数据，如坐标、配置项。")


# ---------- 字典 dict：键值对，按键快速查找 ----------
def show_dict():
    student = {"编号": "101", "姓名": "张三", "项目": "篮球"}
    student["年龄"] = 21          # 新增键值对
    print("字典内容：", student)
    print("student['项目'] ->", student["项目"])
    print("student.get('不存在的键', '无') ->", student.get("不存在的键", "无"))
    print("遍历键值对：")
    for key, value in student.items():
        print(f"  {key}: {value}")

    counts = {}
    for item in ["篮球", "游泳", "篮球", "羽毛球", "篮球"]:
        counts[item] = counts.get(item, 0) + 1
    print("用字典计数：", counts)


# ---------- 集合 set：无序、自动去重、支持集合运算 ----------
def show_set():
    a = {1, 2, 3, 3, 2}
    b = {3, 4}
    print("集合自动去重：", a)
    print("交集 a & b：", a & b)
    print("并集 a | b：", a | b)
    print("差集 a - b：", a - b)
    print("判断元素是否存在：3 in a ->", 3 in a)


def main():
    print("===== 列表 list =====")
    show_list()
    print("\n===== 元组 tuple =====")
    show_tuple()
    print("\n===== 字典 dict =====")
    show_dict()
    print("\n===== 集合 set =====")
    show_set()


if __name__ == "__main__":
    main()
