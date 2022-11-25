class Solution1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def search(x):
            lo, hi = 0, len(nums)  # covers the cases [1]-target :1
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        lo = search(target)
        hi = search(target + 1) - 1

        if lo <= hi:
            return [lo, hi]

        return [-1, -1]


class Solutio2n(object):
    def searchRange(self, nums, target):
        if nums == [] or target not in nums:
            return [-1, -1]

        def FindMin(nums, target):  # We find index left
            low = 0
            hight = len(nums) - 1
            while low <= hight:
                mid = (low + hight) // 2
                print(mid, low, hight)
                if nums[mid] >= target:
                    hight = mid - 1
                else:
                    low = mid + 1

            return low

        def FindMax(nums, target):  # We find index right
            low = 0
            hight = len(nums) - 1
            while low <= hight:
                mid = (low + hight) // 2

                if nums[mid] <= target:
                    low = mid + 1
                else:
                    hight = mid - 1
            return hight

        return [FindMin(nums, target), FindMax(nums, target)]