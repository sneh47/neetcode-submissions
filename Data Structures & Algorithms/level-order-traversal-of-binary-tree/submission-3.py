# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = [root]
        c = []
        r = [root.val]
        c.append(root)
        ret = []

        while q:
            node = q.pop(0)
            if node in c:
                #r = []
                #for n in c:
                #    r.append(n.val)
                ret.append(r)
                c = []
                r = []
            if node.left is not None:
                q.append(node.left)
                c.append(node.left)
                r.append(node.left.val)
            if node.right is not None:
                q.append(node.right)
                c.append(node.right)
                r.append(node.right.val)
        
        return ret