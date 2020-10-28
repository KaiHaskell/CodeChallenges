# Implement the following operations of a queue using stacks.

# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.popStack, self.pushStack = [], []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.pushStack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # I need to move the items from pushstack to popstack before getting rid of the first index
        # check to see if popStack is empty

        if not self.popStack:
            # move items to popStack from pushStack
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        # create a variable to return the removed item
            removed_item = self.popStack.pop()
        # move the items back to pushStack
            while self.popStack:
                self.pushStack.append(self.popStack.pop())
            return removed_item

    def peek(self) -> int:
        """
        Get the front element.
        """
        # exactly the same as pop but I don't delete anything

        if not self.popStack:
            # move items to popStack from pushStack
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        # create a variable to return the item
            peek_item = self.popStack.pop()
            self.pushStack.append(peek_item)
            while self.popStack:
                self.pushStack.append(self.popStack.pop())
            return peek_item

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.pushStack:
            return True
