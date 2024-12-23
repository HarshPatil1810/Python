# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return -1

        # If the node has no children, no second minimum value exists
        if root.left is None and root.right is None:
            return -1

        
        left = self.findSecondMinimumValue(root.left) if root.left.val == root.val else root.left.val
        right = self.findSecondMinimumValue(root.right) if root.right.val == root.val else root.right.val

        if left != -1 and right != -1:
            return min(left, right)
        elif left != -1:  
            return left
        else:  
            return right
        
