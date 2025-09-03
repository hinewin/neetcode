"""
Palindrome checker using Stack and Deque
A palindrome reads the same forwards and backwards
Examples: "racecar", "madam", "A man a plan a canal Panama"
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
    
    def is_empty(self) -> bool:
        return len(self.container) == 0

def is_palindrome_stack(text: str) -> bool:
    """Check palindrome using Stack - builds reversed string"""
    # Clean the text: remove spaces and convert to lowercase
    cleaned = ''.join(text.lower().split())
    
    stack = Stack()
    
    # Push all characters onto stack
    for char in cleaned:
        if char.isalnum():  # Only letters and numbers
            stack.push(char)
    
    # Pop characters to build reversed string
    reversed_text = ""
    while not stack.is_empty():
        reversed_text += stack.pop()
    
    return cleaned == reversed_text

def is_palindrome_deque(text: str) -> bool:
    """Check palindrome using Deque - more efficient approach"""
    # Clean the text: remove spaces and convert to lowercase
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    
    dq = deque(cleaned)
    
    # Compare characters from both ends
    while len(dq) > 1:
        if dq.popleft() != dq.pop():  # Remove and compare front vs back
            return False
    
    return True

def is_palindrome_deque_alternative(text: str) -> bool:
    """Alternative deque approach - using indices instead of popping"""
    # Clean the text
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    
    dq = deque(cleaned)
    
    # Compare using indices (without removing elements)
    while len(dq) > 1:
        front = dq[0]
        back = dq[-1]
        if front != back:
            return False
        dq.popleft()
        dq.pop()
    
    return True

# Test cases
if __name__ == "__main__":
    test_cases = [
        "racecar",
        "hello",
        "madam",
        "A man a plan a canal Panama",
        "race a car",
        "Was it a rat I saw?",
        "Madam, I'm Adam",
        "Never odd or even"
    ]
    
    print("Palindrome Checker Results:")
    print("=" * 50)
    
    for text in test_cases:
        stack_result = is_palindrome_stack(text)
        deque_result = is_palindrome_deque(text)
        
        print(f"'{text}':")
        print(f"  Stack method:  {stack_result}")
        print(f"  Deque method:  {deque_result}")
        print(f"  Match: {'✓' if stack_result == deque_result else '✗'}")
        print()
