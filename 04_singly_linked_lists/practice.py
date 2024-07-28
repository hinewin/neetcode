class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

#Implementation of a singled link list

class LinkedList():
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
