# Design Circular Queue

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the _**MyCircularQueue**_ class:

  + _**MyCircularQueue(k)**_ Initializes the object with the size of the queue to be _**k**_.
  + _**int Front()**_ Gets the front item from the queue. If the queue is empty, return _**-1**_.
  + _**int Rear()**_ Gets the last item from the queue. If the queue is empty, return _**-1**_.
  + _**boolean enQueue(int value)**_ Inserts an element into the circular queue. Return _**true**_ if the operation is successful.
  + _**boolean deQueue()**_ Deletes an element from the circular queue. Return _**true**_ if the operation is successful.
  + _**boolean isEmpty()**_ Checks whether the circular queue is empty or not.
  + _**boolean isFull()**_ Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your programming language. 
### Related Topics
     Array      Linked_List       Design        Queue

### Example:
Example 1:

    Input:
    ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
    [[3], [1], [2], [3], [4], [], [], [], [4], []]
    Output:
    [null, true, true, true, false, 3, true, true, true, 4]

    Explanation:
    MyCircularQueue myCircularQueue = new MyCircularQueue(3);
    myCircularQueue.enQueue(1); // return True
    myCircularQueue.enQueue(2); // return True
    myCircularQueue.enQueue(3); // return True
    myCircularQueue.enQueue(4); // return False
    myCircularQueue.Rear();     // return 3
    myCircularQueue.isFull();   // return True
    myCircularQueue.deQueue();  // return True
    myCircularQueue.enQueue(4); // return True
    myCircularQueue.Rear();     // return 4
    
    
### Constraints

>-  1 <= k <= 1000
>-  0 <= value <= 1000
>-  At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
