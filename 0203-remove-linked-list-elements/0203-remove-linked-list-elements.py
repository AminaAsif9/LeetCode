# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None: # base case
            return head
        
        # checking head
        while head != None and head.val == val: # run loop until head is not none or is equal to val
            head = head.next # if head is equal to val then make head next value, head.
        if head == None:
            return None # as we want to remove

        # checking other values, other than head
        temp = head
        while temp.next != None:
            if temp.next.val != val: # if temp next value not equal to val
                temp = temp.next
            else:
                temp.next = temp.next.next # pointing temp next to temp next next, 
                # means in temp.next is now temp.next.next actually and it's skipping any pointer to next val which is 6
        
        return head