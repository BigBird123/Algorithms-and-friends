# Search in Rotated Sorted Array

There is an integer array _**nums**_ sorted in ascending order (with **distinct** values).

Prior to being passed to your function, _**nums**_ is **possibly rotated** at an unknown pivot index _**k (1 <= k < nums.length)**_ such that the resulting array is _**[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]**_ **(0-indexed)**. For example, _**[0,1,2,4,5,6,7]**_ might be rotated at pivot index _**3**_ and become _**[4,5,6,7,0,1,2].**_

Given the array _**nums**_ **after** the possible rotation and an integer _**target**_, return the index of _**target**_ if it is in _**nums**_, or _**-1**_ if it is not in _**nums.**_

You must write an algorithm with _**O(log n)**_ runtime complexity.

### Related Topics
     Math   Binary_Search
### Example:
  Example 1:
  
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
  Example 2:

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
  Exampple 3:
  
    Input: nums = [1], target = 0
    Output: -1

### Constraints
>- _**1 <= nums.length <= 5000**_
>- _**-104 <= nums[i] <= 104**_
>- All values of **_nums**_ are **unique**.
>- _**nums**_ is an ascending array that is possibly rotated.
>- _**-104 <= target <= 104**_
