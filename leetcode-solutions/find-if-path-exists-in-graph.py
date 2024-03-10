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

        if rootx!=rooty:
            if self.size[rootx]<self.size[rooty]:
                self.parent[rootx]=rooty
                self.size[rooty] += self.size[rootx]
            else:
                self.parent[rooty]=rootx
                self.size[rootx] += self.size[rooty]


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dsu = UnionFind(n)

        for edge in edges:
            dsu.union(edge[0],edge[1])
        
        return dsu.find(source)==dsu.find(destination)

                        
    

        

