class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node

    def insert(self, index, data):
        new_node = Node(data)
        prev = self.head
        for _ in range(index):
            if prev.next == None:
                raise IndexError("Index out of bounds")
            prev = prev.next
        
        new_node.next = prev.next
        prev.next = new_node

    def delete(self, data):
        prev = self.head
        while prev.next:
            if prev.next.data == data:
                prev.next = prev.next.next
            else:
                prev = prev.next
                
    def delete_at(self, index):
        prev = self.head
        for _ in range(index):
            if prev.next == None:
                raise IndexError("Index out of bounds")
            prev = prev.next
        if prev.next is None:
            raise IndexError("Index out of bounds")
        prev.next = prev.next.next
