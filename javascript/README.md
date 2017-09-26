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
var w=10,v10;
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
    - `++`, `--`
+ Comparison
    - `>=`, `<=`, `<`, `>`, `==`, `!=`

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
