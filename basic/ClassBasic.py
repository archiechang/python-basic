# %% __call__
class MyClass1:
    def __init__(self, value: int) -> None:
        self.value = value

    def __call__(self, x: int) -> int:
        return self.value * x


obj = MyClass1(10)
result = obj(5)
print(result)


# %%
class Triangle:
    """三角形类"""

    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    # @classmethod
    # def is_valid(cls, a, b, c):
    #     """判断三条边长能否构成三角形(类方法)"""
    #     return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    def area(self):
        """计算面积"""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


a, b, c = 3, 4, 5
# 静态方法和类方法都是通过给类发消息来调用的
if Triangle.is_valid(a, b, c):
    t = Triangle(a, b, c)
    print(t.perimeter())
    # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
    # print(Triangle.perimeter(t))
    print(t.area())
    # print(Triangle.area(t))
else:
    print("无法构成三角形.")


# %%
class Student1:
    ___slot__ = ("name", "age")

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name or "N/A"

    @property
    def age(self):
        return self._age


stu = Student1("Mike", 20)
print(stu.name, stu.age)

# %%

from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """员工"""

    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

    # @name.setter
    # def name(self, name):
    #     self._name = name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):
    """部门经理"""

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._role = "Manager"

    @property
    def role(self):
        return self._role

    def get_salary(self):
        return 150000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name: str, working_hour: int = 0) -> None:
        super().__init__(name)
        self.working_hour = working_hour
        self._role = "Programmer"

    @property
    def role(self):
        return self._role

    def get_salary(self):
        return 200 * self.working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name: str, sales: int = 0) -> None:
        super().__init__(name)
        self.sales = sales
        self._role = "Salesman"

    @property
    def role(self):
        return self._role

    def get_salary(self):
        return 1800 + self.sales * 0.05


emps = [Manager("James"), Programmer("Michale", 100), Salesman("David", 10000)]
for emp in emps:
    if isinstance(emp, Programmer):
        print(f"Programmer {emp.name} Salary is ${emp.get_salary():.2f}")
    elif isinstance(emp, Salesman):
        print(f"Salesman {emp.name} Salary is ${emp.get_salary():.2f}")
    else:
        print(f"Maneger {emp.name} Salary is ${emp.get_salary():.2f}")

# %%
