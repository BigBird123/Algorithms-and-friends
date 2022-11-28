# Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the _**MinStack**_ class:

  + _**MinStack()**_ initializes the stack object.
  + _**void push(int val)**_ pushes the element val onto the stack.
  + _**void pop()**_ removes the element on the top of the stack.
  + _**int top()**_ gets the top element of the stack.
  + _**int getMin()**_ retrieves the minimum element in the stack.
You must implement a solution with _**O(1)**_ time complexity for each function.
### Related Topics
    Stack        Design


### Example:
Example 1:

      Input:
      ["MinStack","push","push","push","getMin","pop","top","getMin"]
      [[],[-2],[0],[-3],[],[],[],[]]

      Output:
      [null,null,null,null,-3,null,0,-2]

      Explanation:
      MinStack minStack = new MinStack();
      minStack.push(-2);
      minStack.push(0);
      minStack.push(-3);
      minStack.getMin(); // return -3
      minStack.pop();
      minStack.top();    // return 0
      minStack.getMin(); // return -2
      
### Constraints

>-  _**-231 <= val <= 231 - 1**_
>-  Methods _**pop, top, getMin**_ operations will always be called on **non-empty** stacks.
>-  At most _**3 * 104**_ calls will be made to _**push, pop, top, getMin.**_
