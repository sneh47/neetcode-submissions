# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        before = None
        current = head
        
        while current != None:
            after = current.next
            current.next = before
            #after.next = current
            before  = current
            current = after
            #after = current.next
        
        head = before
        return head