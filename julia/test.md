# Julia
# Test notes

We will be defining a Diagonal type

```julia
struct Single Diag { T <:Real}
    diag::Array{ T, 1}
end

# Finding dimensions w/size()
Base.size (sd::SingleDiag) = (length (sd.diag), length(sd.diag))

# Using [] for access
function getindex(sd::SingleDiag, indeices::Vararg{Int, 2})
    (i, j) = indecies
    return i == j? sd.diag[i] : 0
end

function Base.sestindex!(sd::SingleDiag, val, indices::Vararg{Int, 2})
    (i, j) = indices
    if i!=j
        error("Can't assign outside diagg")
    end
    sd.diag[i] = val
    return sd
end
```
- We now have the ability to do the following
    ```Julia
    s = SingleDiag([1, 2, 3, 4, 5])
    @show size(s) # (5, 5)
    @show s[1, 1] # 1
    @show s[1, 2] # 0
    s[1,1] = 10
    @show s # SingleDiag{Int64}
            # ([10, 2, 3, 4, 5])
    ```
- It would be convenient if we had the ability to do any matrix operation but
currently we don't have the ability to do that since we don't have the
operators for our type defined
    - Example
        ```Julia
        t = s + s
        t = s * 2
        t = s * s
        ```
    - We can though if we tell Julia that our type is a subtype of AbstractArray
    This will give you a whole ton of behavior for free.
    ```julia
    struct Single Diag { T <:Real} <:AbstractArray{T, 25}
        diag::Array{ T, 1}
    end
    ```

# Julia type tree
- Three functions you should be aware of
    - Supertype(Integer) # takes any type
    - subtypes(Integer)
        - takes any type and gives back all of it's shild type
    - methods(+)
        - It will return every single method that implements it
    - methods(+, (Integer, Integer)
- Make sure:
    - You're reading from the stable docs!
    - use Julia v0.6.1!
