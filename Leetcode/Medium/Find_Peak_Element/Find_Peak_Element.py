def findPeakElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    low = 0
    hight = len(nums) - 1
    while low < hight:
        mid = (low + hight) // 2
        if nums[mid] > nums[mid + 1]:
            hight = mid
        else:
            low = mid + 1
    return low  #no matter high or low
