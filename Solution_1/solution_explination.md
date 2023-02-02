# **Solution_1_with_only_function**

The function `solve(n)` calculates the number of ways to attend classes over `n` days and the probability that you will miss your graduation ceremony.
<br></br>
___

# **Algorithm**

- If `n` is less than 4, the function returns `2^(n-1)` over `2^n`.
- Initialize the variables `A`, `AA` and `AAA` with the values `2`, `1` and `1` respectively.
- Initialize the variable `P` with the value `4`.
- Initialize the variable `count` with the value `8`.
- Loop `i` from `4` to `n`:
    1. Assign the value of `Z` to `temp`.
    2. Assign the value of `Y` to `Z`.
    3. Assign the value of `X` to `Y`.
    4. Assign the value of `P` to `X`.
    5. Assign the value of `count` to `P`.
    6. Update the value of `count` to `(count - temp) * 2 + temp`.
- Return the result in the format `Z + Y + X` over `count`.
<br></br>

---

# **Complexity**

## Time complexity

```The time complexity of the code is O(n).```

This is because for each iteration in the for loop, the values of X, Y, Z, P, and count are updated in constant time, and the loop is executed n times.


## Space complexity

```The space complexity of the code is O(1).```

This is because the code only uses a small number of variables and their sizes do not depend on the value of n. The values of these variables are updated in each iteration of the loop, so no additional memory is needed.

So, in terms of the input size n, the time complexity is O(n) and the space complexity is O(1).
<br></br>
___

# Tools and Language used

1. Python -- 3.7.2
2. Editor -- VS code


