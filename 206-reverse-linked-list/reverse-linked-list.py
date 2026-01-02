# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = None # step1: initialize prev as none
        # cur = head # step2: start cur at head

        # while cur: # step3: traverse until cur becomes none
        #     temp = cur.next # 4: Store the next node 
        #     cur.next = prev # 5: Reverse the link/pointer
        #     prev = cur # 6: Move prev to current node/forward
        #     cur = temp # 7: Move to the next node/ move cur forward
        # return prev # 8: New head of the reversed list

# other method - not v efficient

        values = [] # array
        curr = head

        while curr: # O(n)
            values.insert(0, curr.val) # insert means storing values in reverse order in array values and at 0 index
            curr = curr.next

        l1 = ListNode(0) # dummy node
        current = l1
        for val in values: # O(n)
            current.next = ListNode(val)
            current = current.next

        return l1.next

        