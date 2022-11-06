# Find Minimum in Rotated Sorted Array
Suppose an array of length _**n**_ sorted in ascending order is **rotated** between _**1**_ and _**n**_ times. For example, the array _**nums = [0,1,2,4,5,6,7]**_ might become:

  - _**[4,5,6,7,0,1,2]**_ if it was rotated _**4**_ times.
  - _**[0,1,2,4,5,6,7]**_ if it was rotated _**7**_ times.

Notice that **rotating** an array _**[a[0], a[1], a[2], ..., a[n-1]]**_ 1 time results in the array _**[a[n-1], a[0], a[1], a[2], ..., a[n-2]].**_

Given the sorted rotated array _**nums**_ of **unique** elements, return the minimum element of this array.

You must write an algorithm that runs in _**O(log n)**_ time.
### Related Topics
     Array     Binary_Search
### Example:
Example 1:
    
    Input: nums = [3,4,5,1,2]
    Output: 1
    Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

    Input: nums = [4,5,6,7,0,1,2]
    Output: 0
    Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times. 
Example 3:

    Input: nums = [11,13,15,17]
    Output: 11
    Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
### Constraints

>- n == nums.length
>- 1 <= n <= 5000
>- -5000 <= nums[i] <= 5000
>- All the integers of nums are unique.
>- nums is sorted and rotated between 1 and n times.
