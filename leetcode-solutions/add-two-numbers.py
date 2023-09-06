# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # def listreverse(list_head):
        #     prev = None
        #     curr = list_head
        #     while curr:
        #         tmp = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = tmp
        #     return prev

        # new_l1 = listreverse(l1)
        # curr1 = new_l1
        # new_l2 = listreverse(l2)
        # curr2 = new_l2
        # num1 = ""
        # num2 = ""
        # while new_l1:
        #     num1+=str(new_l1.val)
        #     new_l1 = new_l1.next

        # while new_l2:
        #     num2+=str(new_l2.val)
        #     new_l2 = new_l2.next
        # # print(num1)
        # # print(num2)
        # res = str(int(num1) + int(num2))
        # # print(res)
        # res = res[::-1]
        # head =None
        # for num in res:
        #     digit = int(num)
        #     new_node = ListNode(digit)
        #     if not head:
        #         head = new_node
        #     else:
        #         curr = head
        #         while curr.next:
        #             curr = curr.next
        #         curr.next = new_node

        # return head


        #optimized solution
        carry = 0
        # tmp1 = l1
        # tmp2 = l2
        l3 = ListNode()
        head = l3
        # head = list3
        while l1 and l2:
            num = l1.val+l2.val+carry
            carry = num//10
            l3.next = ListNode(val=num%10)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            num = l1.val+carry
            carry = num//10
            l3.next = ListNode(val=num%10)
            l3 = l3.next
            l1 = l1.next

        while l2:
            num = l2.val+carry
            carry = num//10
            l3.next = ListNode(val=num%10)
            l3 = l3.next
            l2 = l2.next
        if carry:
            l3.next = ListNode(val=carry)

        return head.next
        
    
            


    


    








        

        

        
        