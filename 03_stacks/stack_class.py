from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, item):
        """ Add item to top of the stack"""
        self.container.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.container.pop()
    
    def peek(self):
        """Return the top item without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.container[-1]
    
    def is_empty(self):
        """ Check if the stack is empty"""
        return len(self.container) == 0
    
    def size(self):
        """Return the number of items in the stack"""
        return len(self.container)
    
    def __str__(self):
        return f"Stack({list(self.container)})"