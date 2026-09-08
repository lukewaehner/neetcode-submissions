# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeList(self, l1, l2):
        d = n = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                n.next = l1
                l1 = l1.next
            else:
                n.next = l2
                l2 = l2.next
            n = n.next 
        n.next = l1 or l2
        return d.next



    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        gap = 1
        while gap < len(lists):
            for i in range(0, len(lists), 2*gap):
                if i + gap < len(lists):
                    lists[i] = self.mergeList(lists[i], lists[i+gap])
            gap = gap * 2
        return lists[0]
