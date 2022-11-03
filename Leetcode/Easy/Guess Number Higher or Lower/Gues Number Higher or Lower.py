# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        hight = n
        while low <= hight:
            mid = (low+hight) // 2
            guess_number = guess(mid)
            if guess_number == 0:
                return mid
            elif guess_number == 1:
                low = mid + 1
            else:
                hight = mid - 1