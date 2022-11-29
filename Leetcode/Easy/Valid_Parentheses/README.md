# First Bad Version

Given a string _**s**_ containing just the characters _**'(', ')', '{', '}', '[', ']'**_  determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.

Every close bracket has a corresponding open bracket of the same type.

### Related Topics
      String        Stack

### Example:
Example 1:
    
      Input: s = "()"
      Output: true
Example 2:

      Input: s = "()[]{}"
      Output: true
Example 3:

      Input: s = "(]"
      Output: false
### Constraints

>-  _**1 <= s.length <= 104**_
>-  _**s**_ consists of parentheses only _**'()[]{}'.**_
