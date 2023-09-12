# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        n = 1 #length of list
        values = []
        tmp = head
        while tmp:
            values.append(tmp.val)
            tmp = tmp.next
        stack = []
        n = len(values)
        result = [0]*n
        for i in range(n):
            while stack and values[stack[-1]] < values[i]:
                stacktop = stack.pop()
                result[stacktop]=values[i]

            stack.append(i)

        return result

