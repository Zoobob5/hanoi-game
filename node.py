class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head)
        self.head = new_node
        self.size += 1

    def remove(self):
        if self.head:
            value = self.head.get_value()
            self.head = self.head.get_next_node()
            self.size -= 1
            return value
        else:
            print("Linked list is empty.")

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def print_list(self):
        current = self.head
        print_list = []
        while current:
            print_list.append(current.get_value())
            current = current.get_next_node()
        print_list.reverse()
        print("Linked List:", print_list)
