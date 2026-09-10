# Definition for singly-linked list.
 #class ListNode:
  #   def __init__(self, val=0, next=None):
   #      self.val = val
    #     self.next = next
#    def __str__(self):
 #       values = []
  #      curr = self

   #     while curr:
    #        values.append(str(curr.val))
     #       curr = curr.next

      #  return " -> ".join(values) + " -> None"

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        
        while curr:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        return prev
