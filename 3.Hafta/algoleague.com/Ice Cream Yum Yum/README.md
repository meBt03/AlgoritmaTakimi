# Ice Cream Yum Yum

## Problem Statement

Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and spend all of their money.

Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

## Function Description

Complete the function `icecreamParlor`:

```python
def icecreamParlor(m: int, cost: List[int]) -> List[int]:
```

- **Parameters:**
  - `m` (int): The amount of money they have to spend.
  - `cost` (List[int]): The cost of each flavor of ice cream.

- **Returns:**
  - `List[int]`: The 1-based indices of the two flavors they buy, sorted in ascending order.

## Input Format

The first line contains an integer, `t`, the number of trips to the ice cream parlor. The next sets of lines each describe a visit:

1. The integer `m`, the amount of money they have pooled.
2. The integer `n`, the number of flavors offered at the time.
3. `n` space-separated integers denoting the cost of each flavor: `cost`.

## Constraints

- \( 1 \leq t \leq 50 \)
- \( 2 \leq n \leq 10^4 \)
- \( 1 \leq cost[i] \leq 10^4 \)
- There will always be a unique solution.

## Sample Input

```
2
4
5
1 4 5 3 2
4
4
2 2 4 3
```

## Sample Output

```
1 4
1 2
```

## Explanation

**Trip 1:**

- They have $4 and there are 5 flavors with costs: [1, 4, 5, 3, 2].
- The flavors at indices 1 and 4 (1-based) have costs 1 and 3, which sum up to 4.

**Trip 2:**

- They have $4 and there are 4 flavors with costs: [2, 2, 4, 3].
- The flavors at indices 1 and 2 (1-based) have costs 2 and 2, which sum up to 4.

