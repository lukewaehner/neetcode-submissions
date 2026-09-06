# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = n = ListNode()
        
        # with two full lists, start merging
        while list1 and list2:
            if list1.val < list2.val:
                # append l1's val
                n.next = list1
                # move l1
                list1 = list1.next
            else:
                # append l2's val
                n.next = list2
                # move l2
                list2 = list2.next
            # move the merged list
            n = n.next
        # append a non-flushed list (or if only given one valid list)
        n.next = list1 or list2
        # move to the head of the merged list (or nothing if both l1 and l2 empty)
        return d.next
            

