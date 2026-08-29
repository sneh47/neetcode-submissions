# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        first = head
        last = head
        # while last.next is not None:
        #     last = last.next
        fast = head
        slow = head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break
            slow = slow.next

        #detach last of first half
        while last.next != slow:
            last = last.next
        last.next = None
        #reverse slow

        #[6, 8, 10]

        print(slow.val)
        prev = None
        current = slow
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            
        #print(prev.val)
        n = prev
        out = []
        while n is not None:
            out.append(n.val)
            n = n.next
        #print(first.val)
        print(out)
        n = first
        out = []
        while n is not None:
            out.append(n.val)
            n = n.next
        print(out)

        #prev and first need to be merged

        #dummy = out = ListNode()

        # 2 4
        # 10 8 6 

        while prev is not None and first is not None:
            f_next = first.next
            first.next = prev
            first = f_next

            p_next = prev.next
            if first is None: break
            prev.next = first
            prev = p_next
            
        #print(prev.val)
        #first.next = p_next

        #return dummy.next
        