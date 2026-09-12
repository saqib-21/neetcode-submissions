# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = ListNode(0)
        print(dum.val)
        dum.next=head
        print(dum.next.val)
        trailer, leader =dum, dum 
        steps = n+1

        while leader:
            if steps !=0:
                leader=leader.next
                steps-=1
                continue
            leader = leader.next
            trailer = trailer.next
        print(trailer.val)
        #print(leader.val)
        if trailer.next == head:
            print("hi")
            trailer.next =trailer.next.next
            trailer=trailer.next
            return trailer
        trailer.next =trailer.next.next
        return head

