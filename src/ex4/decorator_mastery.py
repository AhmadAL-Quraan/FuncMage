from functools import wraps
from typing import Callable
import time
from typing import Any


# What is decorator in python ?
#    function -> take a function and return a function
def spell_timer(func: Callable[[], str]) -> Callable[[], str]:
    @wraps(func)
    def wrapper() -> str:
        print(f"Casting {func.__name__}")
        start = time.perf_counter()
        result = func()
        end = time.perf_counter()
        print(f"spell completed in {end-start:.3f} seconds")
        return result

    return wrapper


@spell_timer
def fireball() -> str:
    time.sleep(0.101)
    return "Fireball cast!"


# A decorator factory:
# is an outter decorator that takes arguments to pass it to the actual one
def power_validator(
    min_power: int,
) -> Callable[..., Any]:
    def decorator(func: Callable[..., str | int]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: int) -> int | str:
            power = args[-1]
            if power > min_power:
                return func(args)
            else:
                return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(
    max_attempts: int,
) -> Callable[..., Any]:
    def decorator(func: Callable[..., None]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper() -> None:
            for i in range(1, max_attempts + 1):
                try:
                    return func()
                except Exception:
                    if i < max_attempts:
                        print(f"Spell failed, retrying...\
(attempt {i}/{max_attempts})")
                    else:
                        print(f"Spell casting failed after\
{max_attempts} attempts")

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        valid_char = True
        valid_length = False
        if len(name) >= 3:
            valid_length = True
        for i in name:
            if not ("a" <= i <= "z" or i == " "):
                valid_char = False

        return True if valid_char is True and valid_length is True else False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@power_validator(40)
def test_power(x: int) -> int:
    return x * x


@power_validator(34)
def test_power2(x: int) -> int:
    return x * x


@retry_spell(3)
def test_retry() -> None:
    raise ValueError()


@retry_spell(3)
def test_retry2() -> str:
    return "Spelled!"


if __name__ == "__main__":
    print("Testing spell timer...")
    print(fireball())
    print(test_power(4))
    print(test_power2(55))
    print("\nTesting retrying spell...")
    test_retry()
    print(test_retry2())
    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("fdd "))
    print(MageGuild.validate_mage_name("fdd& "))
    obj = MageGuild()
    print(obj.cast_spell("fire", 11))
    print(obj.cast_spell("fire", 9))
