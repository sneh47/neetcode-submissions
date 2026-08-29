# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idxs = {}
        for i in range(len(inorder)):
            idxs[inorder[i]] = i
        #print(idxs)
        
        self.preidx = 0
        def dfs(l, r):
            if l > r:
                return None
            #root = TreeNode(preorder[self.preidx])
            #mid = idxs[preorder[self.preidx]]
            #self.preidx +=1

            root_val = preorder[self.preidx]
            self.preidx += 1
            root = TreeNode(root_val)
            mid = idxs[root_val]

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid+1, r)

            return root
        
        return dfs(0, len(inorder)-1)