# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        if not head or not head.next:
            return head
        next_node = curr.next
        while next_node:
            curr.next = prev
            prev = curr
            curr = next_node
            next_node = next_node.next
        curr.next = prev
        return curr