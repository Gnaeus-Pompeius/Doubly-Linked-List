from audioop import reverse
from itertools import count


class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self,):
        self.head = Node()
        self.tail = Node(None, self.head, None)
        self.head.next = self.tail
        self.curr = self.tail

    def __str__(self):
        string = ""
        n = self.head.next
        while n.data != None:
            string += str(n.data) + " "
            n = n.next
        return string

    def __len__(self):
        counter = 0
        variable = self.head.next
        while variable.data != None:
            counter += 1
            variable = variable.next
        return counter

    def insert(self, value):
        self.curr.prev.next = Node(value, self.curr.prev, self.curr)
        self.curr.prev = self.curr.prev.next
        self.curr = self.curr.prev
        
    def remove(self):
        if self.curr == self.head or self.curr == self.tail:
            return
        self.curr.prev.next = self.curr.next
        self.curr.next.prev = self.curr.prev
        self.curr = self.curr.next

    def get_value(self):
        if self.curr == self.tail or self.curr == self.head:
            return
        return self.curr.data

    def move_to_next(self):
        if self.curr.next == self.tail:
            return
        self.curr = self.curr.next

    def move_to_prev(self):
        if self.curr.prev == self.head:
            return
        self.curr = self.curr.prev

    def move_to_pos(self, position):
        counter = 0
        variable = self.head.next
        while variable.data != None:
            if counter == position:
                self.curr = variable
            counter += 1
            variable = variable.next

    def remove_all(self, value):
        variable = self.head.next
        while variable != self.tail:
            if variable.data == value:
                variable.prev.next = variable.next
                variable.next.prev = variable.prev
            variable = variable.next
        if self.curr.data == value:
            self.curr = self.head.next

    def reverse(self):
        temp = None
        current = self.head

        if current.next == self.tail or current.next.next == self.tail:
            return

        while current is not self.tail:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        
        temp = self.head
        self.head = self.tail
        self.tail = temp
        self.head.next = self.head.prev
        self.head.prev = None
        self.curr = self.head.next

    def sort(self):
        num_of_swaps = 1000
        while num_of_swaps != 0:
            num_of_swaps = 0
            current = self.head.next
            
            if current == self.tail or current.next.next == self.tail:
                return

            while current.next != self.tail:
                if current.data > current.next.data:
                    temp = current.data
                    current.data = current.next.data
                    current.next.data = temp
                    num_of_swaps += 1
            
                current = current.next
