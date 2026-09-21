# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s1 = [p]
        s2 = [q]

        while s1:
            n1 = s1.pop()
            n2 = s2.pop()

            if not n1 and not n2:
                continue
            if not n1 or not n2 or n1.val != n2.val:
                return False
        
            s1.append(n1.left)
            s1.append(n1.right)
            s2.append(n2.left)
            s2.append(n2.right)
        return True