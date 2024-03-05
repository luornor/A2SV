class UnionFind:
    def __init__(self,n):
        self.parent = {i : i for i in range(1,n+1)}
        self.size = {i:1 for i in range(1,n+1)}
    
    def find(self,x):
        if self.parent[x]==x:
            return x

        self.parent[x]=self.find(self.parent[x])

        return self.parent[x]
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx!=rooty:
            if self.size[rootx]<self.size[rooty]:
                self.parent[rootx] = rooty
                self.size[rooty]+=self.size[rootx]
            else:
                self.parent[rooty] = rootx
                self.size[rootx]+=self.size[rooty]
        else:
            return [x,y]


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = UnionFind(n)
        # print(dsu.parent)
        res = None
        for u,v in edges:
            res =  dsu.union(u,v)
            if res:
                return res
        
        
