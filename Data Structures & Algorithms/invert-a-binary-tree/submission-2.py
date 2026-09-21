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
        s = [root]

        while s:
            n = s.pop()
            if not n:
                continue
            n.right, n.left = n.left, n.right
            s.append(n.left)
            s.append(n.right)

        return root
