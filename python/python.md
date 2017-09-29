# Python
## Introductory Notes
`Version`: 3.5.2

## Python 2 vs Python 3
+ Unicode Support
+ Backwards incompatible changes to the syntax and default libraries.

## Python Facts
+ Commented lines start with a `#`
```python
# This is a comment line
```
+ `print()` function prints a value to your console over stdout
+ Declare a variable and assign in one step
```python
x = 5
```
+ There is not compile step
+ Whitespace delimited
    - The interperter pays special attention to whitespace instead of curly
      braces in c++
+ 4 spaces per indentation

## Python Constructs
### Types
+ Numbers
    - Int (Integer)
    - Float (FloatingPoint)
+ Boolean (bool)
    - True
    - false
+ str (string)
    - Example
        + "frog's leg"
        + 'frog'
        + ''
        + ""
    - There is not a character type; just single-character strs.
    - iterable
    + None
        - None

### Built-in Data Structures
#### List
- Iterable
- Type is `list`
- Mutable sequence of elements
    ```python
    x = [1]
    x.append(2)
    ```
- Elements may be of differing types
- Examples
    + `[1]`
    + `[1, 2, 3]`
    + `[1, 2, 3, "frog"]`
- Indexing
    + Starts at zero
    + When you index into a List, the index must be an Int
        ```python
        x = ['a', 'b', 'c']
        x[0] # 'a'
        x[500] # IndexError
        x[2] = "frog" # x = ['a', 'b', 'frog']
        ```
    + Negative
        - Counts from the end of the list
        ```python
        x = ['a', 'b', 'c', 'd', 'e', 'f']
        x[-1] # 'f'
        x[-4] # 'c'
        ```

- Slices
    + shallow copy
        - Any sub-lists or sub containers will share memory space with 
          original
    + Start at the first slice index (start index)
    + Stop before the second index (stop index)
    + In set notation `[start_index, stop_index)`
    + Example:
        ```python
        x = ['a', 'b', 'c', 'd', 'e', 'f']
        x[0:2] # ['a', 'b']
        x[3:5] # ['d', 'e']
        x[:4] # ['a', 'b', 'c', 'd']
        x[3:] # ['d', 'e', 'f']
        x[3:1] # []
        x[3:3] # []
        ```
#### Tuple
+ Iterable
+ Immutable sequence of elements
+ Elements can have different types
+ type is `tuple`
+ Examples:
    - `(1,2)`
    - `(1, "frog")`
    - `("frog", )`
        + Comma is very important due to order of operations
    - `()` - Empty tuple
+ Operations with lists:
    ```python
    x = ([1, 2, 3], "frog")
    x[0].append(4) # Will work
    x[0] = "different frog" # Will not work
    ```
+ Indexing
    ```python
    x = (1, "frog")
    x[0] # 1
    x[1] = "apple" # TypeError due to immutability
    ```
    + Negative
        - Works the same as a [list](#list)
+ Slicing
    - Works the same as a [list](#list)

#### Dictionary
+ Iterable (iterates over keys by default)
+ type is `dict`
+ Maps keys to values
+ Keys and values can vary in type
    - Keys `MUST` be hashtable
+ Not a sequence, order does not matter
+ Examples
    ```python
    # Instantiating dicts
    x = {"a": "frog", "b": "giraffe", "c", "apple"}
    y = {"a": "frog", 10: "giraffe", "c", 50} # Varying keys and values 
    z = {} # empty dict

    # Getting Items
    x["a"] # "frog"
    y[10] # "giraffe"
    y["c"] # 50
    x["nope"] # KeyError

    # Setting Items
    x['a'] = "other frog" # mutability
    y[10] = 50 # change to new types
    z["test"] = "test" # {"test": "test"}
    ```

### Custom Types
+ Class-based objects

## Assignment
+ Variables are dynamically typed
    - Can change at runtime
        ```python
        x = 12
        print(type(x)) # <class 'int'>
        x = "frog"
        print(type(x)) # <class 'str'>
        ```
    - Issues with perception of type, may act differently than expected with
      regards to in one part of the program it is an `int` and another part is a
      `string`
+ Python is sort of pointery
    ```python
    x = []
    y = x
    y.append("frog")
    print(x) # ["frog"]
    print(y) # ["frog"]

    ###
    # But
    ###
    x = 10
    y = x
    y = y * 10
    print(x) # 10
    print(y) # 100
    ```

### Unpacking
+ Multiple assignments on one line
+ Example:
    ```python
    (a, b) = (1, 2) # tuple
    a, b = 1, 2 # tuple
    a, b = [1, 2]
    a, b = b, a # swap

    # Numbers need to match
    a, b ,c = 1, 2 # problem
    a, = 1, 2 # problem
    ```

## Operators
+ Arithmetic
    - `+`, `-`, `/`, `*`
        + `/`: Floating point division
            ```python
            5/2 # 2.5
            5.5/3.3 # 1.6666666666666...
            ```
    - `//`: floored quotient
        ```python
        5 // 2 # 2
        5.5 // 3.3 # 1.0
        ```
    - `**`: Exponent
        ```python
        2**3 # 8
        ```
    - `+=`, `-=`, `/=`, `//=`, `*=`, `**=`
        ```python
        a = 2
        a += 2 # a = a + 2
        ```
    - There is no `++` nor `--`
+ Relational operators
    - `==`, `!=`, `>=`, `<=`, `<`, `>`
+ Logical operators
    - `not` equivalent to `!` but there is no `!` in python
    - `or` equivalent to `||`
    - `and` equivalent to `&&`
+ Membership operator
    - `in`
        + returns True or False
            ```python
            x in s # returns True if x is a member of y, otherwise False
            ```
        + Example:
            ```python
            x = [1, 2, 3, 4]
            4 in x # False
            50 in x # False

            y = {"a": 10, "b":50}
            "a" in y # True
            50 in y # False
            50 in y.values() # True
            ```
+ `is`
    - Returns True or False
    - Tests object identity
    - "Don't use it unless you have a good reason to - mwisely 2k17"
    - Example
        ```python
        x = [1, 2, 3]
        y = [1, 2, 3]
        x == y # True
        x is y # False
        ```
    - OK to use to compare w/ None
        ```python
        x = 10
        x is None # False
        x = None
        x is None # True
        ```
    - Pyflakes recommends using 'is' with True and False
        + Either:
            - Have a good reason to compare this way
            - Leave out the comparison:
                ```python
                x = True

                # Doesn't make sense
                if (x is True):
                    foo()

                # Good
                if x:
                    foo()
                ```
## Control Statements
+ `if`, `elif`, `else`
    ```
    if x == 5:
        foo()
    elif x == 6:
        foo()
    elif x == 7:
        foo()
    else: # Must be the end
        foo()
    ```
+ No parentheses around the expression
+ Don't forget the colons
+ No curly braces; watch your indentation (for you c++ programers)
### Truthiness / Falsiness
+ Truthiness  / Falsiness determines whether the conditional evaluates if the
  statement is true or false
    ```
    x = ?
    if x:
        foo()
    ```
+ Falsey values
    - False
    - None
    - Numeric zero (0, 0.0, 0j, ...)
    - Empty string
    - Empty built-in data structures
+ Truthy
    - Anything not listed in `Falsey`
+ bool() function
     ```python
     bool("foo") # True
     bool([]) # False
     ```
+ Be careful when comparing against True and False using `==`
    - Examples:
        ```python
        1 == True # True
        [] == False # False
        bool([]) == False # True
        ```
+ Aside from numeric types, objects of different types don't compare equal
## Loops
+ `while`
    - Pre-check loop
    - No post-check loop in python (No do-while)
    - Leave parentheses off expression
    - Don't forget the colon
    - Example:
        ```python
        while x == 5:
            foo()
            foo()
            foo()

        foo()
        ```
+ `for`
    - Takes an iterable
        + An object that can be yield (return) its members one at a time
        + Examples:
            - list
            - str
            - tuple
            - dict
            - file objects
    + Don't forget the colon
    + "sub-functions"
        - `break`
            + Breaks out of the innermost enclosing loop
        - `continue`
            + Jumps to the next iteration of the loop
        - `pass`
            + strictly a placeholder
        - `else`
            + Executes if the loop completes uninterupted
        - `finally`
            + Runs last no matter what
    + Takes an iterable
    + Example:
        ```python
        for <var> in <iterable>:
            foo()

        for i in [1, 2, 3, 4, 5]:
            if i == 2:
                continue
            if i == 4:
                break
            print(i)
        else:
            print("beep")
        ```

## Higher Order Functions
### Decorators
+ The `@desc` syntax is syntactic sugar for `func = dec(func)`
+ You can stack multiple decorators
    ```
    @d1
    @d2
    def fun():
        pass

    fun = d1(d2(fun))
    ```
+ A decorator will clobber a rapped function's docstring `__name__`, and other
  special attributes.
  - Use functools.wrap to avoid this
```python
import time

def time_this(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        retval = fun(*args, **kwargs)
        stop = time.time()
        print("{} took {:03f} sec".format(func.__name__, stop-start)
        return retval
    return wrapper

@time_this
def add5(x):
    time.sleep(1.0)
    return x+5

add5(10) # 15
#print: Add 5 took 1.001 sec


def add10(x):
    time.sleep(20)
    return x+10

add10=time_this(add10)
```
+ Use Case:
    ```python
    import functools

    def validate_int(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            integer_values = None
            while True:
                try:
                    integer_value = int(func(*args, **args))
                    return integer_value
                except ValueError:
                    print("Requires int")

        return wrapper

    @validate_int
    def prompt_for_age():
        return input("Enter your age: ")

    prompt_for_age()

    ```
+ Example:
    ```python
    def validate(const = int):
        def decorator(func):
            def wrapper(*args, **kwargs):
                retval = None
                while True:
                    try:
                        return const(func(*args, **kwargs))
                    except:
                        print("invalid value")
                return wrapper
        return decorator
    ```

## Map, Filter, and Reduce (aka the math Trinity)
All three are higher order function that work like generator expressions.
+ `map(func, iterable)`
    - Returns a new iterable that yields `func(x)` for each item in the iterable
    - Example
        ```python
        map(str, lst)
        (str(x) for x in lst) # works the same as above
        ```
        The only difference between the two examples above is that
        `map(func, it)` returns a `map` object.
+ `filter(func, iterable)`
    - Returns a new iterable that yields `x` for each item in the iterable
    **only if** `func(x)` is truthy.
    - Example
        ```python
        filter(is_even, lst)
        (x for x in lst if is_even(x))
        ```
+ `functools.reduce(func, iterable [, initial])`
    - applies a function of two arguments cumulatively to the items of
    `iterable` from left to right, so as to reduce an iterable into a
    single value.
    - Example
        ```python
        vals = [0, 2, 4, 6]
        functools.reduce(lambda x, y: x + y, vals) # 12
        functools.reduce(lambda x, y: x + y, vals, 10) # 22
        ```

## Packages
+ Structure a Python's module namespace using "dotted modules names"
```
main.py
classrom/
    __init__.py
    utils.py
    models/
        __init__.py
        assignment.py
``

```python
# main.py
import classroom.utilities
classroom.utilities.grade()

from classroom.models.assignment import Assignment
a = Assignment()
```


# Practice problems
1. Consider the `to_bin()` and `count_forever()` generator functions from class:
    - `to_bin(it)` returns an iterable that converts every item fro it to its
      binary representatino
    - `count_forever(start=0)` returns an iterable that yields start, start+1,
      start+2, ...
    - For each snippet, indicate whether it it terminates or not:
        ```python
        to_bin(count_forever()) # Yes, Generator object
        (bin(x) for x in count_forever()) # Yes, Generator object
        {x:bin(x) for x in count_forever()} # No
        ```
2. Define a function count and a variable in it so that `reduce(count, my_list,
   init)` would reduce a dictionary indicating the number of times each item
   occurs in `my_list`:
   ```python
   from functools import reduce

   my_list = ["they", "were", "the", "best", "of", "times", "they", "were",
              "the", "worst", "of", "times"]

   def count(count_dict, value):
      count_dict.setdefault(value, 0)
      count_dict[value] += 1

      return count_dict


   print(reduce(count, my_list, {}))
   ```

