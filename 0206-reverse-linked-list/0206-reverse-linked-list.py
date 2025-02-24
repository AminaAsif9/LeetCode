# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        
        while cur:
            nextNode = cur.next  # Store the next node
            cur.next = prev      # Reverse the link
            prev = cur           # Move prev to current node
            cur = nextNode       # Move to the next node
        
        return prev  # New head of the reversed list