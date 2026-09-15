# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        seen=[]

        while curr:
            if curr.val in seen:
                if curr.next == None:
                    return False
                if (curr.next.val in seen):
                    return True
            else:
                seen.append(curr.val)
                curr = curr.next 
        return False 
