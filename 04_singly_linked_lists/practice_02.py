class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class SinglyLinkedList():
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if not self.head:
            self.head = Node(value)

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        print (f"Adding {value} before {(self.head)}")
        self.head = new_node
        

    def length_list(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print (count)

    def print_list(self):
        current = self.head
        while current:
            print (current.value, end=" -> ")
            current = current.next
        print (None)

sll = SinglyLinkedList()

sll.append(1)
sll.append("C")
sll.prepend("A")
sll.print_list()
sll.length_list()