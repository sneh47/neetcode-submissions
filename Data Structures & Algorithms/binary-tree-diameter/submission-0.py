# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = 0
        def dfs(node):
            nonlocal maxD
            if node is None:
                return 0
            
            maxhL = dfs(node.left)
            maxhR = dfs(node.right)
            maxD = max(maxD, maxhL + maxhR)
            return max(maxhL, maxhR) + 1

        dfs(root)
        return maxD