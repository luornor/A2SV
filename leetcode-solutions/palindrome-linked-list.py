# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #array solution
        # arr = []
        # while head:
        #     arr.append(head.val)
        #     head = head.next
        # l = 0
        # r = len(arr)-1
        # while l<=r:
        #     if arr[l]!=arr[r]:
        #         return False
        #     l+=1
        #     r-=1

        # return True

        #second solution
        slow = head
        fast = head
        #find the middle index
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #slow is the middle index
        #reverse from middle index
        prev = None
        # temp = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev=slow
            slow=temp

        l = head
        r = prev
        while r:
            if l.val!=r.val:
                return False
            l = l.next
            r=r.next
        return True

        