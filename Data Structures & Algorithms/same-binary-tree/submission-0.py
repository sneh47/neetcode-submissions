# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_q = [p]
        q_q = [q]

        while p_q and q_q:
            p_node = p_q.pop(0)
            q_node = q_q.pop(0)

            if p_node is None and q_node is not None:
                return False
            
            if p_node is not None and q_node is None:
                return False
            
            if p_node is None and q_node is None:
                continue
            elif p_node.val != q_node.val:
                return False
            
            p_q.append(p_node.left)
            p_q.append(p_node.right)
            q_q.append(q_node.left)
            q_q.append(q_node.right)
        
        return True
