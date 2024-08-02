class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with a 'dummy' node which makes
        # Removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head

    # tail should always point to the last node in a linked list
    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        curr = self.head
        while i< index and curr:
            i += 1
            curr = curr.next
        
        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

    def print_list(self):
        cur = self.head.next # skip dummy node
        while cur:
            print (cur.val, end = " -> ")
            cur = cur.next
        print (None)

sll = LinkedList()
sll.insertEnd(1)
sll.insertEnd(2)
sll.insertEnd(3)
sll.print_list()