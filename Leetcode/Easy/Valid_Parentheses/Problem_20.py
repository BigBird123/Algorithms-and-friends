# 1nd solution
class Solution(object):
    def isValid(self, s):
        mapping = {']': '[', ')': '(', '}': '{'}
        stack = []
        for letter in s:
            if letter not in mapping:
                stack.append(letter)
            else:
                if len(stack) > 0:
                    if stack[-1] == mapping[letter]:
                        stack.pop()

                    else:
                        return False
                else:
                    return False

        return len(stack) == 0

# 2nd solution
def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        balanced = True
        index = 0
        while index < len(s) and balanced:
            symbol = s[index]
            if symbol in "([{":
                st.append(symbol)
            else:
                if st == []:
                    balanced = False
                else:
                    top = st.pop()
                    if not matches(top, symbol):
                        balanced = False
            index = index + 1

        if balanced and st == []:
            return True
        else:
            return False