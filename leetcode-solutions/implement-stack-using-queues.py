class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class MyStack:
    def __init__(self):
        self.stack = ListNode()
        

    def push(self, x: int) -> None:
        new_node = ListNode(val=x)
        new_node.next = self.stack
        self.stack = new_node



    def pop(self) -> int:
        if  self.stack:
            val = self.stack.val
            self.stack = self.stack.next
            return val
        else:
            return

    def top(self) -> int:
        if not self.stack:
            return
        else:
            return self.stack.val
    

    def empty(self) -> bool:
        return self.stack.next==None
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()