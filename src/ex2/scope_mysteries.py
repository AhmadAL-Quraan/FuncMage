from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:

    counter = 0

    def counter_func() -> int:
        # Edit must use nonlocal to edit the outer function var
        nonlocal counter
        counter += 1
        return counter

    return counter_func


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    def accumualte_power(extra: int) -> int:
        nonlocal initial_power
        initial_power += extra
        return initial_power

    return accumualte_power


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchantment_des(ench_name: str) -> str:
        return f"{enchantment_type} {ench_name}"

    return enchantment_des


# ... any parameter returns anything
def memory_vault() -> dict[str, Callable[..., Any]]:
    dic: dict = {}

    def store(key: str, value: Any):
        dic[key] = value

    def recall(key: str):
        try:
            return dic[key]
        except Exception as e:
            return f"Memory not found"

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    save = mage_counter()
    save2 = mage_counter()

    print("Testing mage counter...")
    i = 1
    j = 1
    print(f"counter_a call {i}: {save()}")
    print(f"counter_a call {i+1}: {save()}")
    print(f"counter_a call {j}: {save2()}")
    print("\nTesting spell accumulator...")
    base = 100
    accum = spell_accumulator(base)
    print(f"Base {base}, add 20: {accum(20)}")
    print(f"Base {base}, add 30: {accum(30)}")
    ench = enchantment_factory("Flaming")
    print("\nTesting enchantment factory...")
    print(ench("Sword"))
    print(ench("Shield"))
    print("\nTesting memory vault...")
    mapp = memory_vault()
    print(f"Store `secret` = 42 {mapp["store"]("secret",42)}")
    print(f"Recall `secret`: {mapp["recall"]("secret")}")
    print(f"Recall `unknown`: {mapp["recall"]("unknown")}")
