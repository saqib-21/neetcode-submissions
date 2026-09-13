# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr=list1
        twin=list2

        head = front =ListNode(0)
        
        while curr and twin:
            if curr.val <= twin.val:
                head.next = curr
                curr=curr.next
            else:
                head.next = twin
                twin=twin.next
            head = head.next

        head.next = curr or twin

        return front.next