# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = ListNode(0,head)
        trailer, leader =dum, head 
        steps = n

        while leader:
            if steps !=0:
                leader=leader.next
                steps-=1
                continue
            leader = leader.next
            trailer = trailer.next

        trailer.next =trailer.next.next
        return dum.next

