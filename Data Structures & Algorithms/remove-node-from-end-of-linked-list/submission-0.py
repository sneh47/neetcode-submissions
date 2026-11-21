# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        first = head
        while first:
            size +=1
            first = first.next
        second = head
        remove = size - n
        index = 0
        prev = None
        while second:
            if index == remove:
                print(second.val)
                if prev is None:
                    return head.next
                else:
                    prev.next = second.next
                    return head
            index +=1
            prev = second
            second = second.next
            
        
        return head
        