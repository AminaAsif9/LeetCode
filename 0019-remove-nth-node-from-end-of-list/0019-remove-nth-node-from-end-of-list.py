# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create a dummy node that points to head
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move right pointer n steps ahead
        while n > 0 and right:
            right = right.next
            n -= 1

        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next

        # Delete the target node
        left.next = left.next.next

        # Return new head
        return dummy.next        