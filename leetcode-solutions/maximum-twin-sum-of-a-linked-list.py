# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        #find the middle index
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #slow is the middle index
        #reverse from middle index
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev=slow
            slow=temp
        l = head
        r= prev
        max_pair = 0
        while r:
            max_pair = max(max_pair,r.val+l.val)
            r = r.next
            l = l.next

        return max_pair
        
        