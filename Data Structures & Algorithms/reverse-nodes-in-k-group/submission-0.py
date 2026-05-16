# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def kth_after(n: ListNode, k) -> ListNode:
            while n and k > 0:
                n, k = n.next, k - 1
            return n
        
        def reverse(start: ListNode, end: ListNode) -> ListNode:
            curr, prev = start, end

            while curr is not end:
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt
            return prev
        
        dummy = ListNode(0, head)
        grp_prev = dummy
        while True:
            kth_node = kth_after(grp_prev, k)

            if not kth_node:
                break
            start = grp_prev.next
            grp_after = kth_node.next
            grp_prev.next = reverse(start, grp_after)
            grp_prev = start
        return dummy.next



        