# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        tmp = less
        greater = ListNode()
        tmp2 = greater

        while head:
            if head.val<x:
                tmp.next = head
                tmp = tmp.next
            else:
                tmp2.next = head
                tmp2 = tmp2.next
            head = head.next
        tmp.next = None
        tmp2.next = None
        tmp.next = greater.next
        

        return less.next


        