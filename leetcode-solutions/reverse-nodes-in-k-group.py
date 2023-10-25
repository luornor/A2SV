# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(head,k):
            prev = None
            curr = head
            while k>0:
                next_node = curr.next
                curr.next=prev
                prev = curr
                curr = next_node
                k-=1
            return prev

    
        total_nodes = 0
        #count the number of nodes in the list
        tmp = head
        while tmp:
            total_nodes+=1
            tmp = tmp.next
        dummy = ListNode()
        dummy.next = head
        prev_group_end =dummy 
        while total_nodes>=k:
            group_start= prev_group_end.next
            group_end = group_start
            for _ in range(k-1):
                group_end = group_end.next

            next_group_start = group_end.next
            #reverse current group
            group_end.next = None
            reversed_group_start = reverseLinkedList(group_start,k)

            prev_group_end.next = reversed_group_start
            group_start.next = next_group_start
            
            # Update pointers for the next iteration
            prev_group_end = group_start
            total_nodes -= k


        return dummy.next





            


            
        
        