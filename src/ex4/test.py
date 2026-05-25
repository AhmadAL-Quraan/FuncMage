def repeat_message(times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator_repeat


# Applying the factory with an argument


def greet(name):
    print(f"Hello, {name}!")


test = repeat_message(3)
test2 = test(greet)
print(test2("dh"))
