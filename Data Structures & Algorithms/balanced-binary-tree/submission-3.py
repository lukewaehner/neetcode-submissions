# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(r):
            if not r:
                return 0
            left = dfs(r.left)
            if left < 0:
                return -1
            right = dfs(r.right)
            if right < 0:
                return -1
            if abs(left - right) >= 2:
                return -1
            return (1 + max(left, right))
        if not root:
            return True
        return dfs(root) >= 0



