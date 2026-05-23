from functools import reduce


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

def partial_enchanter(base_enchantment: Callable) -> dict[str,Callable]


if __name__ == "__main__":
    l = [1, 3, 4, 5]
    print(spell_reducer(l, ""))
