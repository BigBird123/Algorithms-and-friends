# Guess Number Higher or Lower

Given an array of integers _**nums**_ sorted in non-decreasing order, find the starting and ending position of a given _**target**_ value.

If  _**target**_ is not found in the array, return _**[-1, -1]**_.

You must write an algorithm with _**O(log n)**_ runtime complexity.
### Related Topics
     Array     Binary_Search
### Example:
Example 1:

    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
    
    
Example 2:

    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]
    
Example 3: 

    Input: nums = [], target = 0
    Output: [-1,-1]
### Constraints

>- 0 <= nums.length <= 105
>- -109 <= nums[i] <= 109
>- nums is a non-decreasing array.
>- -109 <= target <= 109
