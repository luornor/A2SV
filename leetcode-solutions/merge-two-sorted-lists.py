# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        temp_curr = temp
        
        while list1 and list2:
            if list1.val<=list2.val:
                temp_curr.next = list1
                temp_curr = temp_curr.next
                list1 = list1.next
            elif list1.val>list2.val:
                temp_curr.next = list2
                temp_curr = temp_curr.next
                list2 = list2.next

        if list1 == None:
            temp_curr.next = list2
        else:
            temp_curr.next = list1
        return temp.next


        