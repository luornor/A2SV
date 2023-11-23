# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #keep the first element of each list in a hep
        heap = []
        for i,arr in enumerate(lists):
            while arr:
                heappush(heap,arr.val)
                arr = arr.next

        dummy = ListNode()
        tmp = dummy
        while heap:
            new = ListNode(val=heappop(heap))
            tmp.next = new
            tmp = tmp.next

        return dummy.next


        
