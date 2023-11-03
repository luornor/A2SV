# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #get to middle of list
        def get_middle(head):
            if not head:
                return head

            fast = head
            slow = head
            while fast.next and fast.next.next:
                slow=slow.next
                fast= fast.next.next

            return slow

        def merge(a,b):
            if a==None:
                return b

            if b==None:
                return a
            l=a
            
            if l.val<b.val:
                l.next = merge(a.next,b)
            else:
                l=b
                l.next=merge(a,b.next)

            return l

        
        if head==None or head.next==None:
            return head
        #find middle of list
        mid = get_middle(head)
        right_side = mid.next
        #split list
        mid.next=None
        #keep splitting list untill end
        a = self.sortList(head)
        b = self.sortList(right_side)

        #then start merging
        return merge(a,b)

        