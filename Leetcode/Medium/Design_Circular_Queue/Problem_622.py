class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self._items = []

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """

        if len(self._items) < self.size:
            self._items.insert(0, value)
            print(self._items)
            return True
        else:
            return False

    def deQueue(self):
        """
        :rtype: bool
        """
        if len(self._items) > 0:
            self._items.pop()
            return True
        else:
            return False

    def Front(self):
        """
        :rtype: int
        """
        if len(self._items) > 0:
            return self._items[-1]
        else:
            return -1

    def Rear(self):
        """
        :rtype: int
        """
        if len(self._items) > 0:
            return self._items[0]
        else:
            return -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        return not bool(self._items)

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self._items) == self.size:
            return True
        else:
            return False

        # Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()