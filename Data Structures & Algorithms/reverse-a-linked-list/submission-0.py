# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        # reverse and get new head(which is last node)
        new_head = self.reverseList(head.next)
        # reverse link bw current node(head) the next node
        (head.next).next, head.next = head, None
        return new_head
