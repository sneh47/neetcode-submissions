# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = root
        t = [root]

        while t:
            node = t.pop(0)
            
            if p.val <= node.val and node.val <= q.val:
                return node
        
            if q.val <= node.val and node.val <= p.val:
                return node
            
            if node.left is not None:
                t.append(node.left)
            if node.right is not None:
                t.append(node.right)

        return lca