from collections.abc import Callable


def test_condition(target: str, power: int) -> bool:
    if power > 40:
        return True
    return False


def fireball(target: str, power: int) -> str:
    return f"fireball at {target} has damaged with {power}"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(
    spell1: Callable[[str, int], str], spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:

    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined


def power_amplifier(
    base_spell: Callable[[str, int], str], multiplier: int
) -> Callable[[str, int], str]:
    def increase(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return increase


def conditional_caster(
    condition: Callable[[str, int], bool], spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return caster


def spell_sequence(
    spells: list[Callable[[str, int], str]],
) -> Callable[[str, int], list[str]]:
    def spell_them(target: str, power: int) -> list[str]:
        results: list[str] = []
        for spell in spells:
            results.append(spell(target, power))

        return results

    return spell_them


if __name__ == "__main__":
    combo = spell_combiner(fireball, heal)
    resu: tuple[str, str] = combo("Dragon", 56)
    print(f"Combined spell result: {resu[0]}, {resu[1]}")
    print("Testing power amplifier...")
    new_spell = power_amplifier(fireball, 10)
    print(f"Original: {fireball('Dragon', 10)}, Amplified:\
{new_spell('Dragon', 10)}")
    condition = conditional_caster(test_condition, fireball)
    print(f"condition failed: {condition("Dragon", 30)}")
    print(f"Condition success: {condition("Dragon", 50)}")
    spells: list[Callable[[str, int], str]] = [fireball, heal]
    spell_apply = spell_sequence(spells)
    gen = (i for i in spell_apply("Dragon", 50))
    try:
        while True:
            print(next(gen))
    except StopIteration:
        pass
