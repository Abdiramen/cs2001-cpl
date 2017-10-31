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

## Variable Declaration
+ Because unused variables are a compiler error, it is common practice to
  declare variables right before you're going to use them
+ Don't worry about trying to declare al variables at the top of a function.

### Constants
+ Automatically deduces type
+ Unused constants are not a compiler error
```go
const A = "frog"
const B string = "frog"
const (
    x string = "frog"
    y int = 10
    z = false
)
```

### Pointers
+ A pointer stores the address of a variable of a given type
```go
var x *int // pointer named x that points to an int 
```
+ Pointer to an array
    ```go
    var y *[3]int // pointer named y that points to an array of 3 ints
    ```
+ The zero value for a pointer in `nil`
+ Go does not permit pointer arithmetic

```go
package main
import "fmt"

func main(){
    x := [3]int{1,2,3} // type: [3]int
    y := x // type: [3]int
    fmt.Println(x) //[1,2,3]
    fmt.Println(y) //[1,2,3]
    y[1] = 10
    fmt.Println(x) //[1,2,3]
    fmt.Println(y) //[1,10,3]
}
```

```go
package main
import "fmt"

func main(){
    x := &[3]int{1,2,3} // type: *[3]int
    y := x // type: *[3]int
    fmt.Println(x) //[1,2,3]
    fmt.Println(y) //[1,2,3]
    y[1] = 10
    fmt.Println(x) //[1,10,3]
    fmt.Println(y) //[1,10,3]
}
```

#### Allocating Memory
+ How do I know if my variables are on the heap or stack?
    - It doesn't matter; don't worry bout it
    - The compiler runtime and garbage collector will handle it for you
+ Functions
    - `new (T)`
        + Allocates storage for a variable of type T at runtime
        + Returns a pointer (*T) pointing to the allocated variable
        + The pointed-to value is zeroed
        ```go
        x := new(int) //*int
        var y *int //*int

        x // 0
        y // nil
        ```
    - `make(T, args)`
        + Creates slices, maps, and channels
        + Returns an initialized value of type `T` (not *T)
            - Slices, maps, and channels require allocation and initialzation
              before use
+ Examples
    ```
    function main(){
        x := new([3]int)
        y := x
        y[1] = 5
        fmt.Println(x) // [0,5,0]
        fmt.Println(y) // [0,5,0]
    }
    ```

## Slices
- Indexed must be non-negative ints
- Accessing index X of array/slice A outside range 0 <= x < len(a) causes a runtime panic

### Creating Slices
- Literal Slice
    - slice of a slice
    ```go
    s := []int{1,2,3,4,5,6}
    s[0] // 1
    t := s[1:3] // [2,3] is a slice
    len(s) // 6
    cap(s) // 6
    t[0] = 1
    s[2] // 1 // s and t share a backing array
    ```
    - slice
    ```go
    s := make([]int, 6,10)
    s[0] // 0
    t := s[1:3]
    len(s) //6
    cap(s) //10
    ```
### Slicing Arrays and Slices
```go
a := [8]int{1,2,3,4,5,6,7,8}
s := a[2:len(a) - 2]
fmt.Println(s) //[3,4,5,6]
s[0] //3
s[1] //4
t = s[1:3] // [4:5]
s[4] // panic
```

# Operators
- The usual C suspects
    - + - * / % : int float complex and str
    - & | ^ : only int
    - << : lhs int
    - >> : rhs int
- `++` and `--` are statements and not expressions
