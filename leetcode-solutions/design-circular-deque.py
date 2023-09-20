class MyCircularDeque:
    def __init__(self, k: int):
        self.deque = [None]*k
        self.size = k
        self.rear = -1
        self.front = -1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear=0
        elif self.front==0:
            self.front=self.size-1
        else:
            self.front-=1
        self.deque[self.front]=value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front=self.rear=0
            self.deque[self.rear]=value
        elif self.rear==self.size-1:
            self.rear=0
            # self.deque[self.rear]=value
        else:
            self.rear+=1
        self.deque[self.rear]=value
        return True
        
        
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.front==self.rear:
            self.front=self.rear=-1
            # self.deque[self.front]=None
        elif self.front==self.size-1:
            # self.deque[self.front]=None
            self.front=0
        else:
            # self.deque[self.front]=None
            self.front+=1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        elif self.front==self.rear:
            # self.deque[self.rear]=None
            self.front=self.rear=-1
        elif self.rear==0:
            # self.deque[self.rear]=None
            self.rear=self.size-1
        else:
            # self.deque[self.rear]=None
            self.rear-=1
        return True


    def getFront(self) -> int:
        if not self.isEmpty():
            return self.deque[self.front]
        else:
            return -1
        
    def getRear(self) -> int:
        if not self.isEmpty():
            return self.deque[self.rear]
        else:
            return -1
        
    def isEmpty(self) -> bool:
        return self.rear==self.front==-1

    def isFull(self) -> bool:
        return  (self.rear==self.size-1 and self.front==0)or(self.front==self.rear+1)


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()