# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        pos = 0

        def kthSmallestHelper(root, k, pos):
            
            if root is None:
                #print("none")
                return (pos, None)
            #print(root.val)
            #if pos == k - 1:
            #    return root.val
            
            #eval left child
            pos, val = kthSmallestHelper(root.left, k, pos)
            if val is not None:
                return (pos, val)
            #eval current
            pos = pos + 1
            if pos == k:
                return pos, root.val
            #eval right child
            pos, val = kthSmallestHelper(root.right, k, pos)
            if val is not None:
                return (pos, val)
            return (pos, val)

        pos, val = kthSmallestHelper(root, k , pos)
        return val
            