# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q = [root]

        while q:
            n = q.pop()
            t = n.right
            n.right = n.left
            n.left = t
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return root
