# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ahead = head
        while n>0:
            ahead = ahead.next
            n-=1
        # If ahead becomes None, 
        #it means n is equal to the length of the list

        if ahead is None:
            return head.next

        behind = head
        while ahead.next:
            behind = behind.next
            ahead = ahead.next
        behind.next = behind.next.next
        return head


        