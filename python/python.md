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
    - Keys `MUST` be hashable
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
+ No curly braces; watch your indentation (for you c++ programmers)
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
+ `bool()` function
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

## Builtin Functions
+ `print(*object, sep=' ', end='\n', file=stdout, fush=False)`
    - Prints things to the text stream (file)
      - Non-keyword arguments are converted to `str` using `str()`
      - Items are separated by `sep`
      - output ends wit `end`
    - If no objects are provided, you'll still see `end`
+ `sorted(iterable[,key][,reverse])`
    - Returns a new sorted list based on the iterable in ascending order. The returned list will be a shallow copy.
    - Not the same as `iterable.sort()` member function
+ `len(thing)`
    - Returns the length of thing
    - works on `str`, `dict`, `list`, `tuple` and some other types, too
+ `help(object)`
    - Opens documentation for that object
    - Useful in the interpreter
    - Quits with q

+ `enumerate(iterable, start=0)`
    - Returns an object of type `enumerate` - an iterable that yields tuples - `(index, value)`.
        ```python
        letters = ['a','b','c','d']
        print( list(enumerate(letters)))
        for i, l in enumerate(letters): # really cool actually
            print(l, "is at index", i)
        ```
+ `range(start, stop[, step])`
    - returns an object of type range which represents an immutable sequence of numbers
    - useful for loop a set number of times.
    - Don't use this as a crutch
    ```python
    L = [1, 2, 3]
    for i, v in enumerate(L): # pretty good idea
          print(v)
          L[i] = 10
    ```
+ `input(prompt-message)`
    - like `cin`; prompts the user and reads from standard in.
+ "Constructors"
    - `int()`, `float()`, `str()`, `list()`, `dict()`, `tuple()`, etc...

## Defining Function
+ Base syntax
    ```python
    def  <function name>(<argument>):
        <body>
    ```
+ Arguments
    - Values must be provided for each argument in order
    - Arguments are always "[passed] by object reference"
        ```python
        def func(s):
            a.append("frog")
            a = ["giraffe"]
            a.append("thingo")
        x = ["apple"]
        y = x
        func(y)
        print(x)
        ```
+ Functions always return something.
    - If you don't explicitly return something from a function, that function will implicitly return `None`.

## Advanced loops
Instead of iterating over every item you can use a slice to skip values.
+ Example
    ```python
    basket = ['Crabapple', 'Banana', 'Pineapple', 'Mango', 'Nectarine']
    message = ['this', 'straight', 'is', 'to ', 'a', 'the, 'message', 'moon']

    for fruit in basket[1:]:
        print(fruit)

    for word in message[::2]:
        print(word)
    ```

### else
Both `while` and `for` have an `else` statement.
- Runs if loop finishes without reaching a `break`.
    - Example
        ```python
        x = 0
        while x < 5:
            print(x)
            x += 1
        else:
            print("beep beep")

        numbers = [5, 6, 7, 8, 9, 10]
        for i in numbers:
            print(i)
        else:
            print('We, counted to 10!')

        ```

## Docstrings
```python
def send_message(sender, recipient, message_body, priority=1):
    """Send a message to a recipient

    :param str sender: The person sending the message
    :param str recipient: The recipient of the message
    :param str message_body: The body of the message
    :param priority: The priority of the message, can be a number 1-5
    :type priority: integer or None
    :return: the message id
    :rtype: int
    :raises ValueError: if the message_body exceeds 160 characters
    :raises TypeError: if the message_body is not a basestring
    """
    # Function definition
```

## Exception Handling

### Errors (Kind of)
+ Syntax Errors
    - your code is bad
    - Python can't read it
    - Example
        ```python
        fr x in [1, 2, 3]:
           print(x)
        ```
    - Python does an initial check prior to interpreting your code.
+ Runtime Errors
    - Your logic is bad
    - Python can't execute it
    - Example
        ```python
        for x in [1, 2, 3]:
            pront(x)
        ```
    - Not found until your code is interpreted
    - Raise Exceptions

### What is Exception Handling?
+ Whenever a runtime error occurs, an exception is raised
+ Helps us track down and fix logical errors

#### How they work:
+ Whenever an exception is raised, it "bubbles up" through the call stack until it is caught **or** it reaches the top (of the call stack).
+ Exceptions (as implied) can be caught and handled.
+ Example
    ```python
    def print_name(person):
        try:
            print(person["name"])
        except KeyError:
            print("Person has no name")
    ```

#### More detail about Exception
+ All exceptions are instances of classes that derive form `BaseException`
+ Most exception you'll use derived from `Exception`
+ There's a big list of built-in exceptions (Don't memorize it since it's a big waste of time and memory)
+ You can also define your own exception (ooh that's cool)
+ Example
    ```python
    # You can keep the caught exception as a variable;
    # useful for error messages and debugging
    try:
        f = open("file.txt")
    except FileNotFoundError as e:
        print("Caught:", e)

    # You can catch several types of Exception with on
    # try-except block
    try:
        print("beep")
        f = open("file.txt")
    except FileNotFoundError:
        something()
    except Is a DirectoryError:
        somthing_else()
    ```
+ try of an `else` clause that works like `for`'s else
+ try also has `finally` which always runs. People use this with database connection often!

## File i/o
### reading
```python
f = open("file.txt")
contents = f.read()
print(contents)
f.close()
```
+ But with the contents manager, `with`, file are automatically closed when you leave the 'with' block.
```python
with open("file.txt") as f:
    print(f.read())
```
### writing
```python
f = open("file.txt", mode="w") # f = open("file.txt, "w")
f.write("stuff")
f.close()

# but this is better
with open("file.txt, mode="w") as f:
    f.write("stuff")
```

## Classes
+ Generally, though not required, classes are written in their own modules.
+ `self` is the calling object
    - you must use `self`{.python} to return to member funcs/vars in the definition of a class
+ member functions are called methods
+ there are no private members.
    - The convention for "don't touch this" is naming with a single underscore.
+ Special member function usually start/end with `__`
    - "overloading operators"
    - Used by constructors

[Wisely's python module](http://cpl.mwisely.xyz/modules/python) has some nice examples and further information

## Modules
+ You can split python projects into multiple files known as modules.
+ You can `import` code `from` one module to another.
+ You can use a module like a library or like a program.
    - You don't run libraries, they have definitions you use.
    - You just use a program.

### Importing
+ `import module`: imports whole module. You can access the members using the dot operator.
+ `from module import thing`: you can import a specific thing from a module also.
+ The import process requires running imported modules.
    - use `if __name__ == "__main__":` if you want your module to run as both a library and a program.

## Variable Argument Lists
```python
def custom_print(*args):  # *args can be any name!
    for i in args:
        print("output:", i)
custom_print(1, 2, 3, 4)


def custom_print2(**kwargs):
    for k,v in kwargs.items():
        print("{}:{}".format(k,v))
```

The function definition for `format()` also uses star arguments: `str.format(*args, **kwargs)`

### Star Magic
```python
# func(a,b,c)
args = ["apple", "banana", "dog"]
func(args) # nope
func(*args) # func(a="apple", b="banana", c="dog")
# length of args has to agree with the number of arguments func() takes

d = {'a': 10, 'b': 12, 'c': 13}
func1(d) # problem
func1(**d) # oh man it works!
```
+ Don't use starmagic without a good reason!
+ Keyword parameters must come after position arguments
+ Arbitrary argument lists comes after positional arguments but before keyword arguments
    - Example
        ```python
        def func(a, b, *args, d=10, e=11, **kwargs):
            pass
        ```

## Comprehensions, Expressions, and Generators
### List Comprehension!!!
```python
    [int(x) for x in["10","20"]] # list created immidiately
```
### Dictionary Comprehension
```python
{k: k.upper() for k in ["a","b"]} # {'a':'A', 'b':'B'}
```

### Generator function!
+ An easy way to make a custom iterable
+ returns an object of type `generator`
+ returns `yields` one item at a time
+ It determines the next item yield on the fly
+ Cannot index; cannot slice
+ Example
    ```python
    def count_forever(start=0):
        i = start
        while True:
            yield i
            i += 1


    for i in count_forever():
        print(x)
        if x == 10:
            break
    ```

### Generator Expressions
```python
    nums = (bin(x) for x in it)
    nums = (bin(x) for x in range(5) if x % 2 == 0)
    # the if statement at the end is called a filtering expression
```

#### A generator expression with multiple for
```python
g = ((x, y) for x in range(3) for y in range(3))
h = ((x, y) for x in range(3) for y in range(x))
nested = (((x, y) for x in range(3)) for y in range(3))
# you can generate generators!!!!
```

## Higher Order Functions
### Decorators
+ The `@dec` syntax is syntactic sugar for `func = dec(func)`
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

### Map, Filter, and Reduce (aka the math Trinity)
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

### Partial Function Application
This is when you call a function but don't give it all the arguments needed.
+ Example
    ```python
    import functools
    def add(x, y)
        return x + y
    add3 = functools.partial(add, 3) # lambda x: add(3, x)
    add3(7) # 10

    take_while_even = functools.partial(take_while, is_even)
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

