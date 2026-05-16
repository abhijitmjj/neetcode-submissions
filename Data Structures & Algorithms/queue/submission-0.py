from dataclasses import dataclass
@dataclass
class Node:
    value:int
    next: 'Node' = None
    prev: 'Node' = None








class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        # create a node
        new_node = Node(value=value)
        # last node
        prev_node = self.tail.prev

        # set the prev to point to this
        prev_node.next = new_node
        # set new_node prev to point to this
        new_node.prev = prev_node
        # now set the tail prev to point to this new_node
        self.tail.prev = new_node

        

    def appendleft(self, value: int) -> None:

        new_node = Node(value=value)

        # get the 1st node
        first_node = self.head.next
        
        # set new node next to this old one
        new_node.next = first_node
        new_node.prev = self.head
        # set head next to this new node
        self.head.next = new_node
        # set its prev to new
        first_node.prev = new_node

        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_node = self.tail.prev
        value = last_node.value

        penultimate_node = last_node.prev

        penultimate_node.next = self.tail
        self.tail.prev = penultimate_node
        return value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first_node = self.head.next
        value = first_node.value

        second_node = first_node.next
        second_node.prev = self.head
        self.head.next = second_node
        return value
        
