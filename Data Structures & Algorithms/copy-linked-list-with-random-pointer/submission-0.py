"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ht = {}
        ht[None] = None
        f = head
        l = 0
        while f:
            ht[l] = (f.val, f.random) # val, r_mem_slot
            f = f.next
            l += 1
        idx_of = {}
        f = head
        j = 0
        while f:
            idx_of[f] = j
            f = f.next
            j += 1

        ht2 = {}
        for j in range(l):
            ht2[j] = Node(ht[j][0])
        ht2[l] = None
        for j in range(l):
            t = ht2[j]
            t.next = ht2[j+1]
            r_val = ht[j][1]
            if r_val == None:
                t.random = ht2[l]
            else:
                t.random = ht2[idx_of[r_val]]
            ht2[j] = t
        return ht2[0]

            
            

