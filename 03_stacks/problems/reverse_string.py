"""
Write a function in python that can reverse a string using stack data structure
reverse_string("We will conquere COVID-19") should return
"91-DIVOC ereuqnoc lliw eW"
"""
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    def push(self, item):
        self.container.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.container.pop()
    def peek(self):
        """Return top item without removing"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.container[-1]
    def is_empty(self) -> bool:
        return len(self.container) == 0
    def __str__(self) -> str:
        return f"Stack({list(self.container)})"
    
def reverse_string(string) -> str :
    print("Reversing...")
    stack = Stack()

    for char in string:
        stack.push(char)

    reverse_string = ''
    
    while not stack.is_empty():
        reverse_string += stack.pop()
    return reverse_string

## Without Class

def reverse_string2(string) -> str:
    """ Deque is only faster if we pop/append from left"""
    stack = []

    for char in string:
        stack.append(char)
    
    reverse_string = ''
    while stack:
        reverse_string += stack.pop()
    return reverse_string


if __name__ == '__main__':
    given_string = "We will conquere COVID-19"
    print (f"String is : {given_string}")
    print (reverse_string(given_string))
    print ("method 2")
    print (reverse_string2(given_string))
    print ("method 3")
    print (given_string[::-1])