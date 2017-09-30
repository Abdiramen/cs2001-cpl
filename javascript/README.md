# Javascript
## Facts
+ Dynamically typed, Untyped, and Interpreted
    - `interpreted` - No compile step
+ Comment lines start with `//`
+ Comment blocks start/end with `/* */`
+ `console.log("stuff");` is how you right to the console
+ **ALWAYS** use semicolons at the ends of statements
## Assignment
+ You can declare / assign variables in several ways
+ Case sensitive
```javascript
var x = 10;
var y;
y = 10;
var w=10,v=10;
```
+ Variables are dynamically typed
+ You can reassign a variable to something of a different type
    ```javascript
    var x = 12;
    console.log(typeof(x)); // number
    x = "bob";
    console.log(typeof(x)); // string
    ```
+ `String` != `string`
+ Pointery
    ```javascript
    "use strict";

    var x = [];
    var y = x;
    x.push("frog");
    console.log(y); // ['frog']
    ```
### Declaration
+ **ALWAYS** use `var`, `let`, or `const` when declaring a variable.
    - Otherwise pollutes global context

```javascript
# f1.js
x = 10;

# f2.js
x = 15;
```
+ X will essentially be a global variable that will transfer across files. If
  you have a common variable name, it would clobber the values.


#### Variable Hosting
Variable declarations float to the top
```javascript
console.log(x===undefined); // true
var x = 3;

// Logically equiavalent
var x;
console.log(x===undefined); // true
x = 3;
```

## Types
### Primitive / values
+ Number - floating point value. Not distinction for int.
+ Boolean - `true` or `false`
+ String
    - Examples
        + 'frog'
        + "frog"
    - No char, just strings of length one
    `- User `.length` for string length
+ Null
    - Used in places where an object can be expected, but no object is
      relevant.
    - There's only one
    - Today, it is rationalized that `null` is considered a placeholder for an
      object even though technically it is a primative value.
    - Would use to return from a function.
    - Signifies absence of value
+ Undefined
    - A variable that has been declared, but not assigned, has value
      `undefined`.
    - Should never be returned explicitly. It is returned from functions if no
      value is explicity returned.
    - Is error-like, if seen something is wrong with the code.
+ Symbol
    - A unique, immutable primitive value
    - Similar to an enumeration
#### Information
+ A primitive is data that is not an object and has no methods (string, number,
  boolean, null, undefined, symbol).
+ They are all immutable
    - `typeof(null)` is object. Widely recognized as a language bug.

#### Primitive Wrapper Objects
```javascript
"frog".toUpperCase(); // "FROG"
// Why does this work with no member methods on primitives?
```
+ Types
    - String for string
    - Number for number
    - Boolean for boolean
    - Symbol for symbol
+ On call of the method, the Javascript engine is creating a new primitive
  wrapper object with the primitive
    ```javascript
    ```javascript
    "frog".toUpperCase(); // "FROG"
    // is equivalent to
    (new String("frog")).toUpperCase()

    (1).toString(); // "1"
    // is equivalent to
    (new Number(1)).toString(); // "1"
    ```
    ```javascript
    typeof(String("frog")); // string primitive
    typeof(new String("frog")); // object
    ```

### Non-primitive
+ Object
    - A collection of properties
    + Properties are parings of key to value
        - Key must be a string 
            + Integers will be casted to strings
        - Values can be anything
    + Object literal syntax
        ```javascript
        x = {id:5, name:"bob", dog:{}};
        ```
    + Defining objects on-the-fly
    ```javascript
    x = null;
    x.id = 5; // Problem

    x = {};
    x.id = 5;
    x.name = "fred";
    x.dog = {};
    ```
+ Arrays
    ```javascript
    a=["hey", "there", , 5]; // Space is fine
    console.log(a[0]); // "hey"
    console.log(a[1]); // "there"
    console.log(a[2]); // undefined
    ```
    - Zero indexed
## Operators
+ `+`, `-`, `*`, `/`, `%`
+ Compound assignment
    - `+=`, `-=`, `*=`, `/=`, `%=`
+ Increment / Decrement
    - Postfix or prefix
        + Same roles as `c++`
    - `++`, `--`
+ Comparison
    - `>=`, `<=`, `<`, `>`, `==`, `!=`, `===`, `!==`

```javascript
var bar = 5;
bar += 2; // 7
var baz = true;
baz += 1; // 2
```
### Concat
```javascript
1 + "foo"; // "1foo"
"foo" + false; // "foofalse"
"foo" + "bra"; // "foobar"
```

### Comparison in-depth
+ When two operands are different types, one of them will be converted to an
  "equivalant" value of the operands type
    - Known as Type coercion
#### Rules
+ Equality (`==`)
    - Converts the operands to the same type prior to making a comparison.
    - Uses the Abstract Equality Comparison Alogrithm
    - Rules are based on type
    - It is not always the guy on the right that's converted
        ```javascript
        1 == 1 // true
        "1" == 1 // true
        1 == "1" // true
        0 == false // true
        0 == null // false
        0 == undefined // false
        null == undefined // true
        ```
+ Inequality (`!=`)
+ Identity / strict equality (===)
    + Can only be true if the operands are already the same type
        ```javascript
        3 === 3; // true
        3 === "3"; // false
        ```
+ Non-identity / strict inequality (!==)
##### Type conversion
+ Number && String
    - String is converted to number
    ```Javascript
    "0" < 3; //true
    "0" > 3; //false
    // "a" -> NaN
    "a" > 3; // false
    "a" < 3; // false
    ```


## Scope
+ Traditionally, block don't have scope, only functions have scope.
    ```javascript
    if (x) {
        stuff();
    }

    // start to end { is block scope
    ```
+ If you delcare a `var` w/ `var` in an ifstatemment, it is visible to the
  whole function.
+ `let` and `const` allow you to create block-scoped variables.

```javascript
"use strict";

function f(){
    var x = 1;
    if(true){
        console.log(z); reference error
        var y = 2;
        let z = 3;
        console.log(x,y,z); // 123
    }
    console.log(x); // 1
    console.log(y); // 2
    console.log(z); // ReferenceError
}

f()

```

## Strict mode
+ An opt-in variant of JS that changes its semantics for the better.
### Usage:
    1. CLI
        ```bash
       node --user-strict
       ```
    2. File:
        ```javascript
        "use strict";
        ```
### Changes
+ It can be applied to entire scripts (programs) or to certain functions.
+ Changes some indeitifers into reserved words
+ Make it impossible ot accidentally create global vars
+ Function params must be unique 
```javascript
"use strict";

yield = 10; // error
y = 10; // error
function f(a, a, b){
    console.log(a,a,b);
}

f(1,5,2); // error

//NON strict mode
f(1,5,2_; // 552
```

## Objects
+ Most values in JS are objects or cna be used as objects.
    + Used as:
        - Boolean
        - String
        - Number
        - Symbol
    + Objects
        - Arrays
        - Functions
        - objects
        - Regular Expressions
# Documentation and other Resources
+ [Mozilla Developer Network (MDN)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
