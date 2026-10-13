# shape_polymorphism —— 图形面积计算

用 Python 面向对象实现图形面积计算，演示**继承与方法重写（多态）**：基类 `Shape`
提供统一的 `area()` 接口，`Circle` 与 `Square` 两个子类分别重写该方法，主程序把
不同子类的实例放进同一个列表，用同一段代码逐个调用 `area()`，由对象的运行时类型
决定实际执行哪个实现。

## 一、项目结构

```
shape_polymorphism/
├── shape.py         # Shape 基类 + Circle / Square 子类
├── main.py          # 主程序：列表 + 遍历调用 area()，体现多态
├── screenshot.png   # 程序运行输出截图
├── output.txt       # 程序运行输出文本（可复制核对）
└── README.md        # 本文档
```

## 二、完整代码思路

### 1. 基类 Shape：定义统一接口

```python
class Shape:
    def area(self):
        return 0
```

`Shape` 是所有图形的抽象约定，只露一个统一的 `area()` 方法，返回 `0`。
基类默认值本身没有实际几何意义，它的作用是规定子类都要有 `area()` 这个方法，
让上层代码可以只认接口

### 2. 子类 Circle：重写 area()

```python
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r
```

`Circle` 用一个实例属性 `r`（半径）描述自己，并**重写** `area()`，
按题目要求用 `3.14 * r * r` 计算圆面积。

### 3. 子类 Square：重写 area()

```python
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
```

`Square` 用实例属性 `side`（边长）描述自己，同样重写 `area()`，
按题目要求用 `side * side` 计算正方形面积。

### 4. 主程序：一个列表，一次遍历

```python
shapes = [Circle(2), Square(3)]

for shape in shapes:
    print(f"{type(shape).__name__} 的面积 = {shape.area()}")
```

列表中同时存放了 `Circle` 和 `Square` 两种不同子类的实例；

循环体里只有一句 `shape.area()`，代码完全相同；

运行时 Python 会根据 `shape` 的真实类型，自动调用对应的 `area()`：
遇到 `Circle` 执行 `3.14 * r * r`，遇到 `Square` 执行 `side * side`。

## 三、运行方法

```bash
python main.py
```

运行结果：

```
Circle 的面积 = 12.56
Square 的面积 = 9
```

- `Circle(2)`：`3.14 × 2 × 2 = 12.56`
- `Square(3)`：`3 × 3 = 9`

运行输出截图见 [screenshot.png](screenshot.png)。

## 四、Git 提交记录（开发历史）

项目按基类、再子类、最后整合的顺序提交，开发历史可通过
`git log --oneline` 查看：

```
feat: 新增 Shape 基类，area() 默认返回 0
feat: 新增 Circle 子类并重写 area() 计算圆面积
feat: 新增 Square 子类并重写 area() 计算正方形面积
feat: 主程序统一遍历列表调用 area() 演示多态
docs: 补充 README 说明完整代码思路
test: 添加运行输出文本与截图
docs: 回填 Git 仓库地址
```

## 五、仓库地址

Git 仓库链接：<https://github.com/scrumo666/AITE-worK>
