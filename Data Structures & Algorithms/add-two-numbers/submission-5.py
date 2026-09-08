# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = m = ListNode()
        c = 0

        while l1 or l2 or c:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            passVal = v1 + v2 + c
            dig = passVal % 10 # the end digit of the value
            c = passVal // 10 # if we have any carryover to move to the next digit during creation
            newNode = ListNode(dig)

            m.next = newNode
            m = m.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return d.next