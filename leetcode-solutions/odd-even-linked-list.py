# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # count = 1
        # odd = ListNode()
        # even = ListNode()
        # oddptr = odd
        # evenptr = even
        # while head:
        #     if count%2!=0:
        #         oddptr.next = head
        #         oddptr = oddptr.next
        #     else:
        #         evenptr.next = head
        #         evenptr = evenptr.next
                
        #     head = head.next
        #     count+=1

        # oddptr.next = None
        # evenptr.next = None
        # oddptr.next = even.next
        # return odd.next
        #second solution
        if not head or not head.next:
            return head
        odd = head #odd index always starts
        even = head.next #followed by even index
        even_head = even #keep track of even list
        # 1->2->3->4->5
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head






        