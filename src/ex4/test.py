from functools import wraps


def check_temp(arg, arg2):
    # decorator factory -> decorator function that takes an arguement
    def decorator(func):

        @wraps(func)
        def wrap(x):
            print(f"{x} {arg}")

            if x <= arg:
                if func.__name__ == "cold":
                    func(x)
                else:
                    print("It's hot not cold")

            if x >= arg:
                if func.__name__ == "hot":
                    func(x)
                else:
                    print("It's cold not hot")

        return wrap

    return decorator


@check_temp(-1, 12)
def cold(x):
    print("Cold ")


@check_temp(1)
def hot(x):
    print("Hot")


# cold = check_temp(-1)(cold)
# cold(1)
print(cold(-1))
print(hot(-1))
