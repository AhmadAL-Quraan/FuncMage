# FuncMage

* Learn about functional programming in python .
<p align="center">
  <img src="pic/meme.jpeg" width="500" alt="Curve meme">
</p>


| Exercise                        | Topic                  |
|---------------------------------|------------------------|
| [Ex0: Lambda Sanctum ](src/ex1) | Lambda functions       |
| [Ex1: Higher realm](src/ex1)    | Higher order functions |
[Ex2: Memory Depths](src/ex2) | Lexical and closure scoping
[Ex3: Ancient Library](src/ex3) | Functools library
[Ex4: Master's Tower](src/ex4) | Decorators and decorator factory design pattern


* Used libraries: `typing`:Type hints, `collections.abc`: Functions type hint (Callable),`functools`: Different useful methods and decorators for functions.



# Lambda functions 

* It's anonymous function (No declaration, just arguments and expression not full body or tough logic).
* Syntax: `lambda arguments : expression` -> returns function object.

* It could be used with different methods to make life easier.
*
| Functions to use with                        |        Used           | Example 
|---------------------------------|------------------------|--------------------------------------------|
|  `map(function, iterable)` | apply specific function on iterables       | `map(lambda x: x+2), array)` return for each value, value + 2
| `filter(function, iterable)`   | Filter items to match specific criteria | `filter(lambda x : x > 3 , array)` check if numbers bigger than 3 or not and return `True` only.
`sorted(iterables, key=function, reverse=True/False)` |sort values, doesn't modifiy original (return new object)  | `sorted(array, key=lambda x : (len(x),x))` -> internally python will map, `value1` -> (6, "value1"), value2 -> (4,"value2"),.. compare by length then by alphabets.
`sum(map())`


* Use lambda functions in simple conditions or functions like above.

## Higher order functions
* These are functions that could take functions as parameters and return a functions.
* Functions accepted as parameters within another functions called "first-class citizens"

* `callable()`: Is a function that return `True` if the object is an `function object` or `False` if it's not.

Ex: 
```python 
# This function takes two functions as arguments 
#where the first one takes int and return int, 
# second one takes int and return string, 
# and the whole function returns a functions that takes an integer and return tuple[int,str]

from collections.abc import Callable

def func(func1:Callable[[int],int], func2:Callable[[int],str]) -> Callable[[int],tuple[Callable,Callable]]: 
   def returned_func(number:int)->tuple[int,str]: 
      return (func1(number),func2(number))
    return returned_func 
```


# Lexical scoping and closure

* Lexical: Is a static scope, dictates that a function’s variable access is determined by its physical placement in the source code.
* Closure: Is only applied in inner function (function inside another), where a function retains access to its lexical scope even after that outer function has finished executing (inner can still see and interact with the variables of the outer).

Ex: 
```python
def outer():
    x = 10  # variable in outer function

    def inner():
        print(x)  # accesses x from outer scope

    return inner

f = outer()  # outer finishes execution
f()          # prints 10
```

* What's happening?
    1) `inner()` is physically written inside `outer()`, so it can access x. This is lexical scoping.
    2) Even after `outer()` finishes, `inner()` **still remembers** x = 10. This is a closure.


--- 

* `nonlocal`: Used only in nested functions to tell the inner one, to edit (inc, dec) the variable of the outer one. 
* Closure that remembers and updates a value (nonlocal)
```python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        print(count)

    return increment

c = counter()

c()  # 1
c()  # 2
c()  # 3
```
*  How do closures enable functions to "remember" their creation environment? Because Inner function keeps a reference to outer function variables. 



# Functools Library 

The `functools` module provides powerful tools for functional programming.

```python
from functools import reduce, partial, lru_cache, singledispatch
```

## reduce()

Reduces an iterable into a single value by repeatedly applying a function.

Example:

```python
from functools import reduce
from operator import add

numbers = [10, 20, 30, 40]

result = reduce(lambda x,y : x + y, numbers)

print(result)  # 100
```

### How reduce works

```text
10 + 20 = 30
30 + 30 = 60
60 + 40 = 100
```

Useful for:

* Summation
* Product calculations
* Finding min/max
* Data aggregation

Example:

```python
from functools import reduce
from operator import mul

powers = [2, 3, 4]

print(reduce(mul, powers))  # 24
```

---

## partial()

Creates a new function with some arguments already filled in.

Example:

```python
from functools import partial

def cast_spell(power, element, target):
    return f"{element} spell ({power}) -> {target}"

fire_spell = partial(cast_spell, 50, "Fire")
ice_spell = partial(cast_spell, 50, "Ice")

print(fire_spell("Dragon"))
print(ice_spell("Goblin"))
```

Output:

```text
Fire spell (50) -> Dragon
Ice spell (50) -> Goblin
```

Benefits:

* Avoid repeated arguments
* Create specialized functions
* Cleaner APIs

---

## lru_cache()

Memoization decorator.

Stores previously computed results.

Example:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(40))
```

Without caching:

```text
fib(40)
 ├─ fib(39)
 ├─ fib(38)
 ├─ fib(39) again
 ├─ fib(38) again
 ...
```

With caching:

* Every Fibonacci number is calculated only once.
* Huge speed improvement.

Cache statistics:

```python
print(fibonacci.cache_info())
```

Example output:

```text
CacheInfo(hits=38, misses=41, maxsize=None, currsize=41)
```

---

## singledispatch()

Function overloading based on argument type.

Example:

```python
from functools import singledispatch

@singledispatch
def spell(obj):
    return "Unknown spell type"

@spell.register
def _(obj: int):
    return f"Damage spell: {obj} damage"

@spell.register
def _(obj: str):
    return f"Enchantment: {obj}"

@spell.register
def _(obj: list):
    return f"Multi-cast: {len(obj)} spells"
```

Usage:

```python
print(spell(42))
print(spell("fireball"))
print(spell([1, 2, 3]))
print(spell(3.14))
```

Output:

```text
Damage spell: 42 damage
Enchantment: fireball
Multi-cast: 3 spells
Unknown spell type
```

---

# Key Takeaways

* `reduce()` aggregates many values into one.
* `partial()` creates specialized versions of existing functions.
* `lru_cache()` provides memoization and major performance improvements.
* `singledispatch()` enables clean type-based behavior.
* Closures allow functions to remember their creation environment.
* `nonlocal` modifies variables in an enclosing scope while preserving encapsulation.
    
---
# Decorators

## 1. Decorators

A decorator is a function that takes another function and returns a modified version of it.

```python
@my_decorator
def greet():
    print("Hello")
```

Equivalent to:

```python
def greet():
    print("Hello")

greet = my_decorator(greet)
```

### Why use decorators?
- Logging
- Timing
- Validation
- Retry logic
- Authentication

This is called **separation of concerns**: the function focuses on its job while the decorator adds extra behavior.

---

## 2. functools.wraps

When wrapping a function, metadata like the function name can be lost.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

Always use `@wraps(func)` in decorators.

---

## 3. Basic Decorator Structure

```python
def decorator(func):

    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result

    return wrapper
```

---

## 4. Parameterized Decorators

Some decorators need arguments.

Example:

```python
@power_validator(10)
def cast(power):
    ...
```

Structure:

```python
def power_validator(min_power):

    def decorator(func):

        def wrapper(*args, **kwargs):
            ...
            return func(*args, **kwargs)

        return wrapper

    return decorator
```

Three nested functions are required.

---

## 5. Retry Decorator

Used when a function may fail.

```python
@retry_spell(3)
def dangerous_spell():
    ...
```

Flow:

```text
Try
 ↓
Fail
 ↓
Retry
 ↓
Success or Give Up
```

Typically implemented using:

```python
try:
    ...
except Exception:
    ...
```

---

## 6. Static Methods

Normal method:

```python
class Mage:
    def cast(self):
        ...
```

Requires an object instance.

Static method:

```python
class Mage:

    @staticmethod
    def validate_name(name):
        ...
```

Can be called as:

```python
Mage.validate_name("Ahmad")
```

No `self` parameter is used.

---

## 7. Instance Method vs Static Method

### Instance Method

```python
def cast_spell(self):
```
- Has access to object data.
- Uses `self`.

### Static Method

```python
@staticmethod
def validate_name(name):
```
- No access to object data.
- Behaves like a normal function that belongs to the class.

---

## 8. Key Takeaways

- Decorators wrap functions.
- `@wraps` preserves metadata.
- Parameterized decorators require three nested functions.
- Retry decorators usually use `try/except`.
- `@staticmethod` methods do not use `self`.
- Decorators help achieve separation of concerns.
