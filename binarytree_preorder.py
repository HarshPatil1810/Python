# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        result = []
    
        def dfs(node):

            if not node:
                return
            
            result.append(node.val)  # Visit root
            dfs(node.left)           # Visit left subtree
            dfs(node.right)          # Visit right subtree
    
        dfs(root)
        return result
        
