# %% クロージャー
def closure(pi):
    def cal(radius):
        return pi * radius * radius

    return cal


c = closure(3.14)
ca2 = closure(3.1415926)

print(f"ca1:{c(10)}")
print(f"ca2:{ca2(10)}")


# %%　decorator
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result

    return wrapper


def decorator2(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        print(args)
        print(kwargs)
        result = func(*args, **kwargs)
        return result

    return wrapper


@decorator1
@decorator2
def add_num(a, b):
    return a + b


r = add_num(10, 20)
print(r)
# %% 输出函数执行时间的装饰器。
from time import time


def record_time(func):
    """自定义装饰函数的装饰器"""

    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f"{func.__name__}:{time()-start}sec")
        return result

    return wrapper


@record_time
def add_num2(a, b):
    return a + b


r = add_num2(10, 20)


# %% __call__


# %%
