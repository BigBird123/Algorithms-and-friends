class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) is None or len(nums) == 0:
            return -1
        low = 0
        hight = len(nums) - 1
        while low <= hight:
            mid = (low + hight) // 2
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]:  # is left rotated:
                if nums[low] <= target <= nums[mid]:  # = is to avoid test cases like [4,5,6,7,0,1,2] target = 0. when nums[low] == target. Ex: 0<0<1 : False -> low = mid+1
                    hight = mid - 1
                else:
                    low = mid + 1
            else:  # right rotated:
                if nums[mid] <= target <= nums[hight]:
                    low = mid + 1
                else:
                    hight = mid - 1
        return -1

