# Graduation Ceremony

This class implements a solution for finding the total number of ways to miss a given number of classes (fixed as 4) in a given number of academic days. The class uses dynamic programming to solve the problem.
<br></br>
___

# Algorithm 

- Initialize the number of academic days `num_academic_days` and the number of missed classes `missed_classes` (fixed as 4).
- Create a 2D list `dp` with `num_academic_days + 1` rows and `missed_classes + 1` columns, and initialize all elements to 0.
- Loop through `i` in the range `0` to `missed_classes - 1` and set `dp[0][i]` to 1.
- Loop through `i` in the range `1` to `num_academic_days + 1` and `j` in the range `missed_classes - 1` to `0` in decrementing order.
- Set `dp[i][j]` to the sum of `dp[i - 1][0]` and `dp[i - 1][j + 1]`.
- Initialize `total_ways_to_attend` with `dp[num_academic_days][0]` and `total_ways_to_not_attend_last_day` with `dp[num_academic_days - 1][1]`.
- Return the result in the form of a string `f"{total_ways_to_not_attend_last_day}/{total_ways_to_attend}"`.
<br></br>
___
 
# Code Break Up

## Class Members
- `x`: an integer representing the total number of academic days.

## Class Methods

### `__init__(self, x)`
The constructor method that initializes the class with the `x` value.

### `solve(self)`
The method that implements the dynamic programming solution to find the total number of ways to miss 4 classes in `x` academic days. The method returns the result in the form of a string in the following format: `total_ways_to_not_attend_last_day/total_ways_to_attend`.

### `execute(self)`
The method that prints the final result by calling the `solve` method.
<br></br>
___

# **Complexity**

## Time complexity

```The time complexity of the code is `O(num_academic_days * missed_classes)`.```

This is because for every academic day i and for every number of missed classes j, the value of dp[i][j] is computed by a constant time operation.


## Space complexity

```The space complexity of the code is O(num_academic_days * missed_classes)```

This is because the 2D list dp is used to store the intermediate results, and its size is proportional to the number of academic days and missed classes.

So, in terms of the number of academic days and missed classes, the space and time complexities are both O(num_academic_days * missed_classes).
<br></br>
___

# Tools and Language used
1. Python -- 3.7.2
2. Editor -- VS code


