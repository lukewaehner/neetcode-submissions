# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(r):
            nonlocal res

            if not r:
                return 0
            left = dfs(r.left)
            right = dfs(r.right)
            if abs(left - right) >= 2:
                res = False
            return (1 + max(left, right))
        if not root:
            return res
        dfs(root)
        return res



