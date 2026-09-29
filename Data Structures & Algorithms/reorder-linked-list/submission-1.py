# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 0. base case (requires None)
        if not head or not head.next:
            return None

        slow, fast = head, head.next
        # 1. split the linked list into two parts:
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        # 2. reverse second half
        prev, curr, future = None, mid, mid.next
        while future:
            curr.next = prev
            prev = curr
            curr = future
            future = future.next
        curr.next = prev
        tail = curr

        # 3. alternating moves
        curr_left, left, curr_right, right = head, head, tail, tail
        while curr_left and curr_right:
            left = left.next
            curr_left.next = curr_right
            curr_left = left

            right = right.next
            curr_right.next = curr_left
            curr_right = right