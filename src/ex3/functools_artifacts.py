from functools import reduce
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
print(enchants["fire"]("hello"))

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

if __name__ == "__main__":
    l = [1, 3, 4, 5]
    print(spell_reducer(l, "add"))
