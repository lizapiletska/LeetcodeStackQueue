import collections

class FreqStack(object):
    """
    Implements a frequency stack.
    """
    def __init__(self):
        """
        Initializes an empty frequency stack.
        """
        self.freq = collections.defaultdict(int)
        self.group = collections.defaultdict(collections.deque)
        self.max_freq = 0

    def push(self, val):
        """
        Pushes an integer val onto the top of the stack.
        """
        self.freq[val] += 1
        freq = self.freq[val]

        group_at_freq = self.group[freq]
        group_at_freq.append(val)

        if freq > self.max_freq:
            self.max_freq = freq

    def pop(self):
        """
        Removes and returns the most frequent element in the stack.
        """
        group = self.group[self.max_freq]
        val = group.pop()

        self.freq[val] -= 1

        if not group:
            if self.max_freq > 0:
                self.max_freq -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()