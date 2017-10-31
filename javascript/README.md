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
+ `typeof`
    ```javascript
    console.log(type_of "frog"); //string
    console.log(type_of 12); //number

    ```

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
"foo" + "bar"; // "foobar"
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
+ Bool && String || Number
    + Bools are converted to numbers
+ Object && String || Number
    + If an object is compared to a string or a number, Javascript will try to
      use the `toString()` method or `valueOf()` method. Otherwise, an error is
      generated
+ Object && Primative
    - Objects are converted to primitive types if compared with a primitive
+ Objects are compared
    ```javascript
    var x = {banana: 10};
    var y = {banana: 10};
    x == y; // False
    ```
    - Does an identity check of memory address of the object


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

## Falsy / Truthy values
### Falsy
+ false
+ null
+ undefined
+ 0
+ NaN
+ empty string ("")
### True
All others.

## Control Structures
+ Block Statements
    ```javascript
    {
        ...
    }
    ```
+ `If/else if/Else`
    ```javascript
    if(foo()){
        ...
    }else if(foo()){
        ...
    }else if(foo()){
        ...
    }else(foo()){
        ...
    }
    ```
+ Switch Statement
    - Fallthrough as in `C++`
    ```javascript
    switch(expression){
        case lab1:
            ... // Will fall through
        case label2:
            ...
            break;
        ...
        default:
            ...
    }
    ```

## Looping Constructs
+ `For`
    ```javascript
    for(let i=0; i < 10; i++){
        ...
    }
    ...
    ```
+ `do-while`
    - Post-check
    ```javascript
    do {
        ...
    }while(expression);
    ```
+ `while`
    - Pre-check
    ```javascript
    while(expression){
        ...
    }
    ```
+ Break
    - Breaks the inner-most enclosing loop statement
        ```javascript
        while(...){
            while(...){
                while(...){
                    if(...){
                        break;
                    }
                }
            }
        }
        ```
    - Except with labels:
        ```javascript
        outerloop:
        while(...){
            while(...){
                while(...){
                    if(...){
                        break outerloop;
                    }
                }
            }
        }
        ```
        + Will break out of the loop labelled


+ Continue
    - Skips to the next iteration of the inner-most enclosing loop
    ```javascript
    while(...){
        while(...){
            while(...){
                if(...){
                    continue
                }
            }
        }
    }
    ```
    - Except with labels:
        ```javascript
        outerloop:
        while(...){
            while(...){
                while(...){
                    if(...){
                        continue outerloop;
                    }
                }
            }
        }
        ```
        + Will skip to the next iteration of the labelled loop

+ `for..in` loop
    + Iterates over all enumerable, distinct properties of an object in
      original insertion order.
        ```javascript
        let obj = {b:2, c:3};
        obj.a = 1;

        for(let x in obj){
            console.log(x);
        }
        // b
        // c
        // a
        ```

        ```javascript
        let lst = ['h','e','l', 'l', 'o']
        lst.name = "hello";

        for(let x in lst){
            console.log(x)
        }
        // 0
        // 1
        // 2
        // 3
        // 4
        // name
        ```
+ `for...of`` loop
    - Iterates over elements of an iterable object:
        - Array
        - String
        - etc.
    ```javascript
    let arr=[3,5,7];
    arr.foo = "bar";

    for(let x of arr){
        console.log(arr)
    }
    // 3
    // 5
    // 7

    for(let x of "abc"){
        console.log(x);
    }
    // a
    // b
    // c
    ```
+ `forEach()` method of Array (like `map`)
    ```javascript
    let arr=[3,5,7];
    arr.forEach(function(value){ //lambda function
        console.log(value)
    })
    // 3
    // 5
    // 7

    arr.forEach(function(value){ //lambda function
        value += 1;
    })
    // 4
    // 6
    // 8

    ```
    + Cannot break or continue
    + Return values are ignored


## Functions
### Basics
```javascript
"use strict";
function multiply(a,b){
    return a*b;
}

multiply(5, 2); // 10
multiply(3,5,4); // 15
multiple(5); // NaN 5 * undefined
```
+ No function overloading
+ First-class because they are objects
+ Have properties
+ Can be passed as a param
+ Can returned from other functions
+ Has higher-order function

### Arguments
```javascript
function (arr){
    arr.push("frog");
    arr = [];
    arr.push("giraffe");
}

var x = [1,2,3];
f(x);
console.log(x) # [1,2,3,"frog"]
```
+ Arguments are passed by value but for objects the value is always a
  reference.
    - "Pass by object reference"
+ `...rest`
    ```javascript
    function concat(...rest){
        let result = "";
        for(lex x of rest){
            result += x;
        }

        return results;
    }

    console.log(concat(1,2,3,4,5)) // "12345"
    ```
+ Default arguments
    ```
    function f(a, b=10){
        // stuff
    }

    f(5); // b is 10
    f(5,6); // b is 6
    ```
### Anonymous Functions
#### Function Expression
```javascript
function foo(){
    return 3;
}

console.log(foo()); // 3
log(foo); // [Function]

var bar = function(){
    return 3;
}

log(bar()) // 3
log(bar); // [Function]
```

```javascript
var sq = function(x){
    return x*x;
}
```

```javascript
// F is a function
function map(f, a){
    let result = [];

    for(let x of a){
        result.push(f(a))
    }

    return result;
}

map(function(x){return x*x;}, [1,2,3]);
// [1,4,9]
```
#### Arrow Expression
```javascript
map((x)=>{return x*x;}; [1,2,3]);
```
+ Defines a function that does not bind certain values:
    - this
    - super
    - arguments
    - etc...
+ Is not appropriate to use as an object method (member function).
+ Is sort of like a python lambda function

### Function scoping & Hoisting
+ Functions must be in scope to be called
+ Function declarations are hoisted (both name and def), but function
  expressions are not.
```javascript
log(square(5)); // 25
function square(x){return x*x;}
```
```javascript
log(square(5)); // TypeError (not defined)
var square = function(x){return x*x;};
```

```javascript
"use strict";
let num1=10, num2=3;

function multiply(){
    var x = 20;
    return num1 * num2;
}

console.log(multiply()); // 30
console.log(x); // ReferenceError
```

```javascript
fucntion get_score(){
    let name = "leopard", points = 50;
    function format_score(){
        return name + ": " + points;
    }

    return format_score;
}

console.log(get_score); // [Function]
console.log(get_score()); // [Function]
console.log(get_score()()); // [String]
```

### Immediately invoked function expression (IIFE)
+ Sytnax
    ```javascript
    (function(){ .... })();
    ```

```javascript
let foo = (function(){...});
foo(); // (function(){...})();
```

```javascript
var x = (function(){return 3;})();
log(x); // 3
```

### Function Closures
+ Functions that can retain access to internal variables but not accessible by
  outside scope
```javascript
let sum=0;
function acc(num){
    sum += num;
    console.log(sum);
}

acc(4); // 4
acc(5); // 9
sum = 0;
acc(3); // 3
```

```javascript
function acc(num){
    let sum = 0;
    sum += num;
    console.log(sum);
}

acc(4); // 4
acc(5); // 5
sum = 10; // reference error
```

```javascript
function acc_factory(){
    let sum = 0;
    return function(num){
        sum += num;
        log(sum);
    };
}

let acc = acc_factory();
acc(4); // 4
acc(5); // 9
let foo = acc_factory(); // New `sum` variable
foo(3); // 3
```

```javascript
var acc = (function(){
    let sum = 0;
    return function(num){
        sum += num;
        console.log(sum);
    };
})();

acc(4); // 4
acc(5); // 9
sum = 10; // reference error
```

```javascript
// acc only increments by 5
var acc = (function(num){
    let sum = 0;
    return function(){
        sum += num;
        console.log(sum);
})(5);

acc() // 5
acc() // 10
```

## Importing
+ All files are automatically wrapped in an IIFE, making imports harder
+ `require` keyword works a alot like import
+ All files must be explicitly exported using `module` object.
```javascript
//main.js
// IIFE
(function(){
    varfuncs = require("./funcs.js")
    funcs.foo(); // logs "foo"
})();
```

```javascript
//funcs.js
// IIFE
(function(){
    function foo(){
        console.log("foo");
    }

    // key:value pair of what you want to export
    module.exports = {foo: foo};
    // or
    module.exports = foo;
    // There is also exports
})();
```
### Exports and imports
+ ES6 added `export` and `import` Keywords that make Js feel more like Python
  and company
+ They don't work w/ most JS engines if you're going to use them, you need a
  tanspiler like Babel.
+ We'll only use module.exports in CPL

## Asynchrony
### Call Function Stack
```javascript
// main.js
function multiply(a,b){
    return a*b;
}

function square(n){
    return multiply(n,n)
}

function logSquare(n){
    let n2 = square(n)
    console.log(n2);
}

logSquare(10);
```
1. On the very bottom of our call stack will be the `main.js IIFE`.
2. Then `logSquare(10)` is pushed to the call stack.
3. Then, `square(10)` will be pushed to the call stack.
4. Then, `multiply(10,10)` will be pushed to the call stack.
5. `Mulitply` will be popped, returning 100.
6. `Square` will be popped returning 100.
7. `console.log(n2)` is pushed to the call stack.
8. `console.log(n2)` is popped off the stack.
9. `logSquare` is popped off the call stack.
10. The `main.js IIFE` will be popped off the call stack.

```javascript
(function f(){
    console.log("frog");
    f();
})();
// Stack overflow
```

### Event Queue
+ Event Queue passes data to the call stack when the call stack is clear

### Asynchronous Programming and Callbacks
```javascript
'use strict';

const fs = require('fs');
const log = console.log;

// fs.readdir takes a directory and callback. A function to be called after
execution of the function.
fs.readdir('./stuff', function(err, files){
    if(err != null){
        log("Uh oh!");
        return;
    }

    if(!files.includes("my_file.txt"){
        log("Uh oh!");
        return;
    }

    fs.readFile('./stuff/my_file.txt', function(err, data){
        if(err != null){
            log("Uh oh!");
            return;
        }

        if(!files.includes("my_file.txt"))j{
            log("Uh oh!");
            return;
        }

        let new_data = data + "beep\n";
        fs.writeFile("./stuff/my_file.txt", new_data, function(err){
            if(err != null){
                log("Uh oh!");
            }

            fs.readFile('./stuff/my_file.txt', function(err, data){
                log("my_file.txt now contains...");
                log(data);
            });
        });
    });
});
```

### Promises
+ A promise object...
    - represents the eventual completion (or failure) of an async options, as
      well as its resulting value.
    - Allows you to associate handlers (functions) iwth an async actions
      eventual success or failure reason.
    - Is in one of three states:
        1. **pending** - initial state
        2. **fulfilled** - success state
        3. **rejected** - failure state
    - Instead of registering callbacks, we tell a Promise what to do if a
      computation succeeds or fails:
        1. `.then(<succes handler>)`
            a. If you succeed, then do this.
        2. `.catch(<failure handler>)`
            a. If you fail, then catch the error and do this.
+ Modern JS libraries use Promises a lot.
+ Not all libraries are written to use Promises.
+ Node v 6.11 has `Promise`
+ Node v 8.x also has Promise & `utils.promisify()`

#### Promise Chaining
+ Promise `.then()` returns promises which can then be acted on.

#### Example
```javascript
'use strict`;
// Creating a promise out of a Node-style callback function
const readFileP = function(path){
    return new Promise(
        function(resolve, reject){
            fs.readFile(path, fucntion(err,data){
                if(err != null){
                    reject(err);
                }else{
                    resolve(data);
                }
            });
        }
    );
}


// Using promise
readdirP('./stuff/').then(
    function(files){
        if(!files.includes("my_files.txt")){
            raise "Oh no!";
        }

        return readFileP('./stuff/my_file.txt');
    }
).then(
    function(data){
        let new_data = data + "beep";
        return writeFileP('./stuff/my_file.txt', new_data);
    }
).then(
    function(){
        return readFileP('./stuff/my_file.txt');
    }
).then(
    function(data){
        console.log("Message");
        console.log(data);
    }
).catch(
    function(err){
        console.log("Uh oh!");
    }
);
```


## Templating
+ MISSING: Objects, new operators, prototypes, etc.



# Documentation and other Resources
+ [Mozilla Developer Network (MDN)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

# Review Questions
+ Fill in the blanks using words from the work bank:
    - It is acceptable to explicitly return **null** from a function. We never
      explicitly return **undefined**.
+ Question 2
    ```javascript
    function f(){
        var x;
        console.log(x); # Undefined
    }

    f();
    console.log(x); # Exception
    ```
    - Explain what happens when the program is run. Include ouput of a
      description of any errors encountered.
        - The function will log undefined within the function due to
          function-level hoisting.
        - The `console.log(x)` at the bottom will create an exception
+ Draw the stack, queue, event loop, and Node.js. Show the state of each
  component 2.5 seconds after the program started. Label and describe:
    ```javascript
    'use strict';

    console.log('A');
    setTimeout(function tina() (){
        sonole.log('B');
    }, 3000);

    setTimeout(function gene(){
        setTimeout(function louise(){
            console.log('C');
        }, 2000);

        console.log('d');
    }, 2000);

    console.log('E');
    ```
