class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        count = 0
        temp = self.head
        while temp:
            if count==index:
                return temp.val
            count+=1
            temp = temp.next
        return -1

        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        # if not self.head:
        #     head = new_node
        new_node.next = self.head
        self.head = new_node
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        #check if list is empty
        if not self.head:
            self.head=new_node
        else:
            temp = self.head
            while temp and temp.next:
                temp = temp.next
            temp.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        count=0
        new_node = Node(val)
        temp = self.head
        if index==0:
            new_node.next = self.head
            self.head = new_node
            return
        #find the position
        prev = None
        while temp and count!=index:
            prev = temp
            temp = temp.next
            count+=1
        if count!=index:
            return
        prev.next=new_node
        new_node.next = temp

        
    def deleteAtIndex(self, index: int) -> None:
        # if not head:
        count = 0
        temp = self.head
        if index==0:
            self.head = temp.next
        else:
            prev = None
            while temp and count!=index:
                prev = temp
                temp=temp.next
                count+=1

            if not temp:
                return
            if prev:
                prev.next = temp.next


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)