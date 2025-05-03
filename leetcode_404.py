# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node):
            sum_left=0
            if not node:
                return 0
            if  node.left and not node.left.left and not node.left.right:
                sum_left+=node.left.val
            sum_left+=dfs(node.left)
            sum_left+=dfs(node.right)
            return sum_left
        
        return dfs(root)
        
                
            
                
    
