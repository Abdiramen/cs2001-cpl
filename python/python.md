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
    + Stop before the secinod index (stop index)
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
+ Iterable (iterates ove rkeys by default
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
+ Aside from numeric types, objets of different types don't compare equal
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
    
