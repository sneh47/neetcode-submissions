"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        ht = {}
        #key = value, value = node
        if node is None:
            return
        #print(node.val)
        #for n in node.neighbors:
            #print(n.val)

        q = deque([node])
        root = None
        visited = set()
        while q:
            n = q.popleft()
            if n.val not in ht:
                #this should only be for root
                current_node = Node(n.val)
                ht[current_node.val] = current_node
                visited.add(current_node.val)
            else:
                current_node = ht[n.val]
            if root is None:
                root = current_node
            
            
            for neighbor in n.neighbors:
                if neighbor.val in ht:
                    current_node.neighbors.append(ht[neighbor.val])
                else:
                    #create the neighbor
                    new_node = Node(neighbor.val)
                    current_node.neighbors.append(new_node)
                    ht[new_node.val] = new_node
                    
                if neighbor.val not in visited:
                    q.append(neighbor)
                    visited.add(neighbor.val)

        
        return root