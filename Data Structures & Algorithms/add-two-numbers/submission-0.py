# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def build_number(self, l):
        s = []
        while l:
            s.append(l.val)
            l = l.next
        res = 0
        i = 0
        while i < len(s):
            v = s[i]
            res += v * (10 ** i)
            i += 1
        return res

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        print(self.build_number(l1))
        print(self.build_number(l2))
        nv = str(self.build_number(l1) + self.build_number(l2))
        print(nv)

        d = n = ListNode()
        for c in nv[::-1]:
            n.next = ListNode(c)
            n = n.next
        return d.next