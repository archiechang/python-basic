# %% import
from typing import Callable, Optional

# %%変数
item_1: str = "a"
item_2: int = 10
item_3: float = 3.14
item_4: bool = True
item_5: bytes

item_list: list[str] = ["a", "b", "c"]

item_tuple: tuple[str, int, str] = ("a", 1, "b")
item_tuple2: tuple[str, ...] = ("a", "b", "c")

item_dict: dict[str, int] = {"a": 1, "b": 2}

item_set: set[int] = {1, 2, 3, 4}

print(item_list)
print(item_tuple)
print(item_dict)
print(item_set)


# %% NONE
# Noneになる可能性のある値には`Optional[]`を使用する
def some_function() -> None:
    pass


x: str | None = some_function()  # Python 3.10+
print(x)
x: Optional[str] = some_function()
print(x)

# Mypyは 以下のif文(if-statement)中でxがNoneならないことを理解できます。
# Mypyを利用する場合は、x.upperのようなメソッド(を利用)がエラーにならないようにするには
# 一度 if文を利用して None でないことを確認する必要があります。
x = None
if x is not None:
    print(x.upper())

# ある不変条件によって値がNoneにならない場合は、assertを使用します。
x = "abc"
assert x is not None
print(x.upper())


# %%　関数
def func_sample1(item_1: int, item_2: float) -> float:
    return item_1 * item_2


def func_sample2(item_1: int, item_2: float) -> None:
    print(item_1, item_2)


print(func_sample1(3, 2.1))
func_sample2(1, 5)

# %% Lambda
zf2: Callable[[int], str] = lambda s: str(s).zfill(2)
print(zf2)


# %% Union 複合型
def process_item(item: int | str):
    print(item)


process_item(100)
process_item("abc")

# %% Optional
item: Optional[str]
item: str | None

# %%
