"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 1) Weave: A -> A' -> B -> B' ...
        cur = head
        while cur:
            nxt = cur.next
            cur.next = Node(cur.val, nxt, None)
            cur = nxt

        # 2) Point: set random for copies
        cur = head
        while cur:
            copy = cur.next
            copy.random = cur.random.next if cur.random else None
            cur = copy.next

        # 3) Unweave: split originals and copies (A -> A' -> B -> B'-> ...)
        # curr = A, copy = A' === curr.next; curr.next = copy.next; copy.next = copy.next.next curr = cur.next
        cur = head
        clone_head = head.next
        while cur:
            copy = cur.next
            cur.next = copy.next                 # restore original
            copy.next = copy.next.next if copy.next else None
            cur = cur.next

        return clone_head

