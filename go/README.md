# Go
+ Compiled
    - You can run small programs with `go run`
    - Build bigger projects or single files with `go build` or `go install`
+ Other Subcommands
    - `go fmt` - format code 
    - `go doc` - displays package documentation
+ Statically typed
+ Comments
    - Lines: `//` 
    - Blocks: `/* */`
+ `fmt.Println()` is one way to write to standard out
    - requires importing of `fmt`

## Built-in types
+ Boolean
    - bool
        + Predeclared constants: `true`, `false`
+ Numeric
    - Unsigned integers
        + `uint`, `unit8`, `uint16`, `uint32`, `uint64`
            - `unit` is either 32-bits or 64-bits based on compiler
              implementation
    - Signed integer types
        + `int`, `int8`, `int16`, `int32`, `int64`
            - `int` is either 32-bit or 64-bit depending on implementation
    - IEEE-754 floating point types
        + `float32`, `float64`
            - Default is `float64`
    - Complex number types
        + `complex64`, `complex128`
            - default is `complex128`
    - Byte
        + `byte`
            - Alias for uint8
            - Not converted to/from uint8 automatically
    - Rune
        + `rune`
            - Represents a Unicode code point
            - Like a char, but not a char
            - An alias for `uint32`
            - No automatic conversion
+ Strings
    - String
        + `string`
            - A possibly empty sequence of bytes
            - Immutable
            - Length checked with `len(string)`
            - Must use `"`
+ Arrays
    - Array
        + `array`
            - `[<number of elements>]<element_type>]`
                + `<number of elements>` must be constant
                + `<number of elements>` is included in the type
            - Indexed starting at 0
            - Length checked with `len(array)`
        + `slice`
            - `[]<element_type>`
            - "... a descriptor for a contiguous element of an underlying array
              ..."
            - Backed by an array w/ a set capacity
            - Indexed starting at 0
            - Length w/ `len(slice)`
            - Capacity w/ `cap(slice)`
                + Length of the backing array
+ Absence of value
    - `nil`


## Variable Declaration/Assignment
+ Explicit type
    ```go
    var x int;
    var x,y,z int;

    var x int = 1;
    var x,y,z int = 1,2,3;
    ```

+ Implicit type
    ```go
    x := 10 // int
    x,y,z := 1,2,3 // ints
    a,b,c := "a", 10, false
    ```
    
    ```go
    i := 42 // int
    j := 50.5 // float64
    k := 0.5 + 10i // complex128

    var i int64 = 42;
    ```

+ Examples
    - Array
        ```go
        var myArray [10]int;
        myArray[1] = 1;
        fmt.Println(myArray); // [0 1 0 ... 0]
        ```
        - You can rely on go to initialize all variables to the type default
    - Slices
        ```go
        var myThirdSlice []int // fundamentally different
        myOtherSlice := []int{}
        mySlice := []int{10,12,14,16}
        fmt.Println(mySlice); // [10 12 14 16]
        ```
+ Uninitialized variables are given a zero-value by default
    - 0 for numeric types
    - false for bool
    - empty string for string
+ The compiler will enforce proper use of types
    ```go
    x := 12 // int
    x = 10 // fine
    x = "frog" // no
    x = 12.5 // no
    ```
+ The compiler will not implicitly convert types
    - No type coercion in go
        ```go
        i := 42
        y := 5.5
        fmt.Println(i + y) // NO!
        fmat.Println(float64(i) + y) // YES!
        ```
+ `_` is the blank identifier
    - Used for ignoring unwanted values
