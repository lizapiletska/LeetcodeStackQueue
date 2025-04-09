"""
Implement_Queue_using_Stacks
"""
class Node:
    """
    A node.
    """
    def __init__(self, value=None):
        """
        Initializes a new node.
        """
        self.value = value
        self.next = None


class Stack:
    """A stack."""
    def __init__(self):
        """
        Initializes an empty stack.
        """
        self._top = None

    def is_empty(self):
        """
        Checks if the stack is empty.
        """
        return self._top is None

    def push(self, value):
        """
        Pushes a new value onto the stack.
        """
        node = Node(value)
        node.next = self._top
        self._top = node

    def pop(self):
        """
        Removes and return top of stack.
        """
        if self.is_empty():
            raise IndexError("Pop from the empty stack")
        result, self._top = self._top.value, self._top.next
        return result

    def peek(self):
        """
        Returns top of stack without removing.
        """
        if self.is_empty():
            raise IndexError("Peek from the empty stack")
        return self._top.value


class MyQueue:
    """
    A queue.
    """
    def __init__(self):
        """
        Initializes the queue.
        """
        self._input_stack = Stack()
        self._output_stack = Stack()

    def push(self, x):
        """
        Adds an element to the end of the queue.
        """
        self._input_stack.push(x)

    def transfer_stacks(self):
        """
        Additional method to transfer elements from input to output stack.
        """
        if self._output_stack.is_empty():
            while not self._input_stack.is_empty():
                self._output_stack.push(self._input_stack.pop())

    def pop(self):
        """
        Removes and return front of queue.
        """
        self.transfer_stacks()
        return self._output_stack.pop()

    def peek(self):
        """
        Returns front of queue without removing.
        """
        self.transfer_stacks()
        return self._output_stack.peek()

    def empty(self):
        """
        Checks if queue is empty.
        """
        return self._input_stack.is_empty() and self._output_stack.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()