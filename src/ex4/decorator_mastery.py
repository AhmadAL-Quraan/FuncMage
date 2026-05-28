from functools import wraps
from typing import Callable
import time


# What is decorator in python ???????????????????????????///////// function -> take a function and return a function
def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(arg1):
        print(f"Casting {func.__name__}")
        print(arg1)
        start = time.perf_counter()
        result = func()
        end = time.perf_counter()
        print(f"spell completed in {end-start:.3f} seconds")
        return result

    return wrapper


@spell_timer
def fireball():
    time.sleep(0.101)
    return "Boom"


# A decorator factory: is an outter decorator that takes arguments to pass it to the actual one
def power_validator(
    min_power: int,
) -> Callable[[Callable[[int], int]], Callable[[int], int | str]]:
    def decorator(func: Callable[[int], int]) -> Callable[[int], int | str]:
        @wraps(func)
        def wrapper(power: int) -> int | str:
            if power > min_power:
                return func(power)
            else:
                return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(
    max_attempts: int,
) -> Callable[[Callable[[], None]], Callable[[], None]]:
    def decorator(func: Callable[[], None]) -> Callable[[], None]:
        @wraps(func)
        def wrapper() -> None:
            for i in range(1, max_attempts + 1):
                try:
                    return func()
                except Exception:
                    if i < max_attempts:
                        print(
                            f"Spell failed, retrying... (attempt {i}/{max_attempts})"
                        )
                    else:
                        print(
                            f"Spell casting failed after {max_attempts} attempts"
                        )

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

        return True if valid_char == True and valid_length == True else False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"

    cast_spell = power_validator(10)(cast_spell)


@power_validator(40)
def test_power(x: int) -> int:
    return x * x


@power_validator(34)
def test_power2(x: int) -> int:
    return x * x


if __name__ == "__main__":
    print(test_power(4))
    print(test_power2(55))
