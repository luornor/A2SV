# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = None
        # current = head
        # while current:
        #     temp = current.next
        #     current.next = prev
        #     prev=current
        #     current=temp
        # return prev

        
        if head==None:
            return head
        
        if head.next==None:
            return head

        next_ptr = self.reverseList(head.next)

        head.next.next = head
        head.next = None


       

    
        return next_ptr

        

        


        

        