# Guess Number Higher or Lower

Given a **sorted** integer array _**arr**_, two integers _**k**_ and _**x**_, return the _**k**_ closest integers to _**x**_ in the array. The result should also be sorted in ascending order.

An integer _**a**_ is closer to _**x**_ than an integer _**b**_ if:

    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b
### Related Topics
    Array     Two_Pointers      Binary_Search     Sliding_Window      Sorting Heap_(Priority_Queue)

### Example:
Example 1:

    Input: arr = [1,2,3,4,5], k = 4, x = 3
    Output: [1,2,3,4]
Example 2:

    Input: arr = [1,2,3,4,5], k = 4, x = -1
    Output: [1,2,3,4]
### Constraints

>- 1 <= k <= arr.length
>- 1 <= arr.length <= 104
>- arr is sorted in **ascending** order.
>- -104 <= arr[i], x <= 104
