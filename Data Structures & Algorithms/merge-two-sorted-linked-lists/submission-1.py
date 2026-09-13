# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr=list1
        twin=list2

        head = ListNode(0)
        front=head
        #my sol 
        while curr or twin:
            #if blanks lists 
            if curr == None:
                head.next = twin
                twin=twin.next
                head = head.next
                continue
            if twin == None:
                head.next = curr
                curr=curr.next
                head = head.next
                continue
            #normal two pointer checks
            if curr.val <= twin.val:
                head.next = curr
                curr=curr.next
            else:
                head.next = twin
                twin=twin.next
            #move to next check
            head = head.next
        return front.next