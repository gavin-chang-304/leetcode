# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = float('-inf')
        
    def maxPathSum(self, root: TreeNode) -> int:
        ''' find the max sum of child for each node '''
        
        self.dfs(root)
        return self.res
    
    def dfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # find the max sum for left chlid
        left = max(self.dfs(root.left),0)
        
        # find the max sum for right child
        right = max(self.dfs(root.right),0)
        self.res = max(self.res, left+right+root.val)
        
        return max(left,right,0)+root.val