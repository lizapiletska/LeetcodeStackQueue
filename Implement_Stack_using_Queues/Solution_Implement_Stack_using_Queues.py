from collections import deque

class Node:
    """
    A node for storing data in a linked list.
    """
    def __init__(self, value=None):
        """
        Initializes a new node.
        """
        self.value = value
        self.next = None


class Queue:
    """
    A queue.
    """
    def __init__(self):
        """
        Initializes the queue.
        """
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        """
        Checks if the queue is empty.
        """
        return self.front is None

    def push(self, item):
        """
        Adds an element to the end of the queue.
        """
        new_node = Node(item)

        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def pop(self):
        """
        Removes and returns the front element of the queue.
        """
        if self.is_empty():
            return None
        dequeued_value = self.front.value
        self.front = self.front.next
        self.size -= 1
        if self.is_empty():
            self.rear = None
        return dequeued_value

    def peek(self):
        """
        Returns the front element of the queue without removing it.
        """
        if self.is_empty():
            raise IndexError("Peek from the empty queue")
        return self.front.value

    def _iter(self):
        """
        Additional method. Iterates through the queue from front to rear.
        """
        current = self.front
        while current:
            yield current
            current = current.next

    def __len__(self):
        """
        Returns the size of the queue.
        """
        return self.size

    def __str__(self):
        """
        String representation of the queue.
        """
        return " -> ".join(str(node.value) for node in self._iter())


class MyStack(object):
    """
    A stack.
    """
    def __init__(self):
        """
        Initializes the stack.
        """
        self.queue = Queue()

    def push(self, x):
        """
        Push element onto stack.
        """
        self.queue.push(x)
        for _ in range(len(self.queue) - 1):
            self.queue.push(self.queue.pop())

    def pop(self):
        """
        Removes and returns the element from the top of the stack.
        """
        return self.queue.pop() if not self.queue.is_empty() else None

    def top(self):
        """
        Returns the element from the top of the stack without removing it.
        """
        return self.queue.peek() if not self.queue.is_empty() else None

    def empty(self):
        """
        Returns True if the stack is empty, False otherwise.
        """
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
