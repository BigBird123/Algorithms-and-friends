class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        hight = x
        while low <= hight:
            mid = (low + hight) // 2
            if (mid*mid) == x:
                return mid
            elif (mid*mid) < x < (mid+1) * (mid+1):
                return mid
            elif mid*mid > x:
                hight = mid - 1
            else:
                low = mid + 1
        return mid