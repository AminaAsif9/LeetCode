# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy node to start the merged list
        curr = dummy  # Pointer to build the new list

        while list1 and list2:  # Iterate until one list is exhausted
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next  # Move to the next node
        
        # Attach the remaining nodes of the non-empty list
        curr.next = list1 if list1 else list2  

        return dummy.next  # Return the merged list (excluding dummy node)