# Design Circular Queue
Given an array of integers _**temperatures**_ represents the daily temperatures, return an array _**answer**_ such that _**answer[i]**_ is the number of days you have to wait after the _**ith**_ day to get a warmer temperature. If there is no future day for which this is possible, keep _**answer[i] == 0**_ instead.



### Related Topics
    Array       Stack       Monotonic_Stack

### Example:
Example 1:

      Input: temperatures = [73,74,75,71,69,72,76,73]
      Output: [1,1,4,2,1,1,0,0]
      
Example 2:

      Input: temperatures = [30,40,50,60]
      Output: [1,1,1,0]

Example 3:

      Input: temperatures = [30,60,90]
      Output: [1,1,0]
### Constraints

>-  1 <= temperatures.length <= 105
>-  30 <= temperatures[i] <= 100
