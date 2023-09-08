class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next = next
class MyCircularQueue:

    def __init__(self, k: int):
        self.size=k
        self.head = None
        self.tail = None
        self.count = 0
    
        
    def enQueue(self, value: int) -> bool:
        if self.count<self.size:
            new_node = ListNode(val=value)
            if self.head is None:
                new_node.next =self.head
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.count+=1
            return True
        else:
            return False



    def deQueue(self) -> bool:
        if self.count>0:
            self.head =self.head.next
            self.count-=1
            return True
        else:
            return False

        

    def Front(self) -> int:
        if self.count>0:
            return self.head.val
        else:
            return -1
        

    def Rear(self) -> int:
        if self.count>0:
            return self.tail.val
        else:
            return -1
        

    def isEmpty(self) -> bool:
        return self.count==0
        
    def isFull(self) -> bool:
        return self.size==self.count
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()