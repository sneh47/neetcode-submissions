# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new = None
        head = None
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                if new is not None:
                    new.next = list1 
                    new = new.next
                else:
                    new = list1
                    head = new
                list1 = list1.next
            else:
                if new is not None:
                    new.next = list2
                    new = new.next
                else:
                    new = list2
                    head = new
                list2 = list2.next
            
        if list1 is not None:
            if new is not None:
                new.next = list1 
                new = new.next
            else:
                new = list1
                head = new
        if list2 is not None:
            if new is not None:
                new.next = list2 
                new = new.next
            else:
                new = list2
                head = new

        return head