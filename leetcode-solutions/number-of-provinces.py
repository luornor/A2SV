class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n

    def find(self,x):
        if self.parent[x]==x:
            return x
        self.parent[x]=self.find(self.parent[x])

        return self.parent[x]

    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx != rooty:
            if self.size[rootx]<self.size[rooty]:
                self.parent[rootx]=rooty
                self.size[rooty]+=self.size[rootx]
            else:
                self.parent[rooty]=rootx
                self.size[rootx]+=self.size[rooty]

    def connected(self,x,y):
        return self.find(x)==self.find(y)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dis_join = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]== 1 and i!=j:
                    dis_join.union(i,j)
          
        connected = set()
        for i in range(n):
            parent = dis_join.find(i)
            connected.add(parent)

        return len(connected)


        
         

