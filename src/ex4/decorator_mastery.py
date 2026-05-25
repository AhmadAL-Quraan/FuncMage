from functools import wraps
from typing import Callable
import time


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
def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(power: int, *args, **kwargs):
            if power > min_power:
                return func(power, *args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper

    return decorator


@power_validator(40)
def test_power(x):
    return x * x


@power_validator(34)
def test_power2(x):
    return x * x


if __name__ == "__main__":
    print(test_power(4))
    print(test_power2(55))
