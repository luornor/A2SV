# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        idx = 1
        while prev.next and idx<left:
            prev = prev.next
            idx+=1

        current = prev.next
        while current and idx<right:
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
            idx += 1
        return dummy.next
        