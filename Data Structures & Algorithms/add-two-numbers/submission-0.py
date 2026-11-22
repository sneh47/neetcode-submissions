# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumlist = ListNode(0)
        head = sumlist
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            sumdigits = val1+ val2 + carry
            if sumdigits >= 10:
                carry = 1
            else:
                carry = 0
            
            sumlist.next = ListNode(sumdigits%10)

            sumlist = sumlist.next
            l1 = l1.next if l1 is not None else l1
            l2 = l2.next if l2 is not None else l2
        
        return head.next