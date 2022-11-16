class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        hight = len(s)-1
        newS = list(s)
        while left < hight:
            s[left] = newS[hight]
            s[hight] = newS[left]
            left = left + 1
            hight = hight - 1