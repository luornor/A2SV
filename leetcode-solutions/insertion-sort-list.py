# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # arr = []
        # while head:
        #     arr.append(head.val)
        #     head = head.next
        # for i in range(1,len(arr)):
        #     j = i
        #     while j>0 and arr[j-1]>arr[j]:
        #         arr[j-1],arr[j] = arr[j],arr[j-1]
        #         j-=1
        # start = None
        # for num in arr:
        #     new_node = ListNode(val=num)
        #     if not start:
        #         start = new_node
        #     else:
        #         tmp = start
        #         while tmp and tmp.next:
        #             tmp = tmp.next
        #         tmp.next = new_node

        # return start


        # temp = current.next
        # current.next = prev.next
        # prev.next = current
        # current = temp
        dummy = ListNode(next=head)
        curr = head.next
        prev = head        
        while curr:
            if curr.val>=prev.val:
                prev = curr
                curr = curr.next
            else:
                tmp = dummy
                while tmp.next.val<curr.val:
                    tmp = tmp.next
                #insert before previous node
                prev.next = curr.next
                curr.next = tmp.next
                tmp.next = curr
                curr = prev.next
                
        
        return dummy.next





            