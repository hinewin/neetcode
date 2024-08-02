## Personal Notes
In computer science, a `singly linked list` is a data structure that consists of a sequence of elements called `nodes`. Each node holds two values:

**The Value** - this could be any kind of data type or object (integer, string, etc)

**Reference (or link)** to the next node in the sequence - this is usually a pointer that points to the next node

A singly linked list allows for efficient insertion and removal of elements from any position in the sequence during iteration. However, singly linked lists by themselves do not allow random access to the data, or any form of efficient indexing.

```python
# First, define a Node class
class Node:
    def __init__(self, data=None):
        self.data = data    # Hold the data
        self.next = None    # And a reference to the next node. Initialize it as None.


# Then, define a Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None.

    # Method to add new node at the end of the list (append to the list)
    def append(self, data):
        # If there isn't any node yet, 
        # then create a new Node and designate it as the head
        if not self.head:
            self.head = Node(data)
        # If there are previous nodes, 
        else:
            cur = self.head
            # Traverse to the end of the list
            while cur.next:
                cur = cur.next
            # Append the new node at the end
            cur.next = Node(data)

    # Print method to visualize the list
    def print_list(self):
        cur = self.head # Start from the head
        while cur:
            print(cur.data, end=' -> ')
            cur = cur.next
        print(None)    # Print None at the end of the list

# Usage:
sll = SinglyLinkedList()
sll.append('A')
sll.append('B')
sll.append('C')
sll.print_list()  # Outputs: A -> B -> C -> None
```