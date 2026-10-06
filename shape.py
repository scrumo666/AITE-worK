"""形状类层次结构：用于演示面向对象的多态特性。"""


class Shape:
    """形状基类。

    area() 作为统一接口，默认返回 0；
    具体形状的子类通过重写该方法给出各自的面积计算方式。
    """

    def area(self):
        return 0


class Circle(Shape):
    """圆形，用半径 r 描述，面积 = 3.14 * r * r。"""

    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


class Square(Shape):
    """正方形，用边长 side 描述，面积 = side * side。"""

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
