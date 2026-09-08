# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            # generate a sentinel
            dummy = ListNode(0, head)
            l = 0
            f = head
            # find the length of the array
            while f:
                f = f.next
                l += 1
            # start before the array
            prev = dummy
            for _ in range(l - n):
                prev = prev.next
            prev.next = prev.next.next
            # shift into the actual array
            return dummy.next