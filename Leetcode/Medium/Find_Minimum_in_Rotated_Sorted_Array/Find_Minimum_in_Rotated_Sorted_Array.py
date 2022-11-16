class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Suggestion from solver:
            All the elements to the left of inflection point > first element of the array.
            All the elements to the right of inflection point < first element of the array.
        """
        low = 0
        hight = len(nums) - 1
        while low < hight:
            mid = (low + hight) // 2
            if nums[low] <= nums[mid]:
                if nums[low] <= nums[mid] <= nums[hight]:
                    return nums[low]
                else:
                    low = mid + 1
            else:
                hight = mid
        return nums[low]
