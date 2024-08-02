"""
Singly linked list implementation
"""

class Node:
    """
    Define a Node class with value and next as reference point
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    """
    Define a Singly Linked List class
    """
    def __init__(self):
        self.head = None # Initialize head of the list as None

    def append(self, value):
        """
        Method to add new node at end of list (Append to the list)
        """
        # If there isn't any node yet,
        # then create a new Node and designate it as the head
        if not self.head:
            self.head = Node(value)
        # If there are previous nodes already,
        else:
            cur = self.head
            # Traverse to the end of the list
            while cur.next:
                cur = cur.next
            # Append the new node at the end
            cur.next = Node(value)
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        curr = self.head
        # If HEAD node is to be deleted
        if curr and curr.value == key:
            self.head = curr.next
            curr = None
            return
        
        prev = None
        while curr and curr.value != key:
            prev = curr
            curr = curr.next
        
        # key not found in list
        if not curr:
            return
        
        # Unlink the node from linked list
        prev.next = curr.next
        curr = None

    def print_list(self):
        """
        Print method to visualize list
        """
        # Start from head
        cur = self.head
        while cur:
            # `end` sets what string gets printed at end of each print statement
            print (cur.value, end=' -> ') 
            cur = cur.next
        # Print None at end of list
        print (None)

# Usage

sll=SinglyLinkedList()
sll.append("A")
sll.append("B")
sll.append("123")
sll.append(456)

sll.print_list() # Output: A -> B -> 123 -> 456 -> None
