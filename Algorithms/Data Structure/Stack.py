class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.top is None:
            raise IndexError("pop from empty stack")
        data = self.top.data
        self.top = self.top.next
        return data
    
    def print_all(self):
        current = self.top
        while current:
            print(current.data, end = " ")
            current = current.next