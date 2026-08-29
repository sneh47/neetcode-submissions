# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValidBSTHelper(root, ul, ll):
            if root.left is None and root.right is None:
                #print(root.val)
                if root.val > ll and root.val < ul:
                    return True
                else:
                    return False
            
            if root.left is None:
                #process right
                #print("onlyright")
                #print(root.val , root.right.val,ul, ll)
                if root.val < root.right.val and root.val > ll and root.val < ul:
                    return isValidBSTHelper(root.right, ul, root.val)
                else:
                    return False
            if root.right is None:
                #print("onlyleft")
                #print(root.val , root.left.val, ul, ll)
                if root.val > root.left.val and root.val > ll and root.val < ul:
                    return isValidBSTHelper(root.left, root.val, ll)
                else:
                    return False
            
            if root.val < root.right.val and root.val > root.left.val and root.val > ll and root.val < ul:
                #print(root.val , root.right.val, root.left.val, ul, ll)
                return isValidBSTHelper(root.left, root.val, ll) and isValidBSTHelper(root.right, ul, root.val)
            else:
                #print(root.val , root.right.val, root.left.val, ul, ll)
                return False
        
        return isValidBSTHelper(root, 1000000000, -1000000000)