from functools import lru_cache, reduce, singledispatch
from typing import Any
from collections.abc import Callable
import functools


# reduce the values into one value by applying some function one by one on values
def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(lambda x, y: x + y, spells)
    elif operation == "multiply":
        return reduce(lambda x, y: x * y, spells)
    elif operation == "max":
        return reduce(lambda x, y: max(x, y), spells)
    elif operation == "min":
        return reduce(lambda x, y: min(x, y), spells)
    if len(operation) != 0:
        print("operation not known")
    return 0


def partial(power: int, element: str, target: str):
    return f"{element} enchantment with power {power} cast on {target}"


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> dict[str, Callable]:
    return {
        "fire": functools.partial(base_enchantment, 50, "fire"),
        "ice": functools.partial(base_enchantment, 50, "ice"),
        "lightning": functools.partial(base_enchantment, 50, "lightning"),
    }


enchants = partial_enchanter(partial)


# key: arguments : value = return
@lru_cache(maxsize=100000)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


# def multiply(x, y, **kwargs):
#     return x * y * kwargs["key"]
#
#
# double = lambda y: multiply(2, y, key=4)
# print(double(3))
#
# # Patirl better for readability and slightly faster
# double2 = functools.partial(multiply, 2, key=3)
# print(double2(4))
#


# Named like this because it's dispatch on the first argument only
def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def handle(data: Any) -> str:
        return "Unknown spell type"

    @handle.register
    def _(data: int) -> str:
        return f"Damage spell: {data} damage"

    @handle.register
    def _(data: str) -> str:
        return f"Enchantment: {data}"

    @handle.register
    def _(data: list) -> str:
        return f"Multi-cast: {len(data)} spells"

    return handle


if __name__ == "__main__":
    l = [1, 3, 4, 5]
    print("Testing spell reducer...")
    spells = [1, 2, 3, 4, 5, 6, 6, 7, 8, 8, 10]
    print(f"Sum: {spell_reducer(spells,"add")}")
    print(f"Product: {spell_reducer(spells,"multiply")}")
    print(f"Max: {spell_reducer(spells,"max")}")
    print()
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print()
    print("Testing partial_enchanter...")
    print(f"{partial_enchanter(partial)["fire"]("dragon")}")
    print("\nTesting spell dispatcher...")
    func = spell_dispatcher()
    print(func(42))
    print(func("fireball"))
    l = ["one", "two", "three"]
    print(func(l))
    print(func(3.45))
