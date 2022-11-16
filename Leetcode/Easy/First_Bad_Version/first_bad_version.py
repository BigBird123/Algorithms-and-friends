#Solution 1
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        hight = n
        while low <= hight:
            mid = (low + hight) // 2
            if isBadVersion(mid) == True:
                hight = mid - 1
            else :
                low = mid + 1
        return low
#Solution 2:
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        Because the smaller the number of True, it's the 'First Bad Version'
        We will search on the left immediately,
        then based on that to consider the search conditions and space.
        """
        low = 1
        hight = n
        # Importantly, there is no equal. Since we search left immediately and 'hight' doesn't add 1
        while low < hight:
            mid = (low + hight) // 2
            if isBadVersion(mid) == True:
                hight = mid
            else:
                low = mid + 1

        return hight  #no matter high or low, we do binary search to the last element