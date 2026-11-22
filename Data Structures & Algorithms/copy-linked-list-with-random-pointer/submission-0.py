"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldnew = {}
        oldnew[None]= None

        cur = head
        while cur:
            new = Node(cur.val)
            oldnew[cur] = new
            cur = cur.next

        cur = head
        while cur:
            oldnew[cur].next = oldnew[cur.next]
            oldnew[cur].random = oldnew[cur.random]
            cur = cur.next
        
        return oldnew[head]