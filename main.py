"""主程序：把不同形状放进同一个列表，统一调用 area() 体现多态。"""

from shape import Circle, Square


def main():
    # 列表元素类型都是 Shape 的子类实例，但它们各自的 area() 行为不同
    shapes = [Circle(2), Square(3)]

    for shape in shapes:
        # 同一行调用代码，实际执行哪个 area() 由对象的运行时类型决定
        print(f"{type(shape).__name__} 的面积 = {shape.area()}")


if __name__ == "__main__":
    main()
