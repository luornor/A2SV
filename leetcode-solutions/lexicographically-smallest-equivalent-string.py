class UnionFind:
    def __init__(self):
        self.parent = {c:c for c in list(string.ascii_lowercase)}
    
    def find(self,x):
        if self.parent[x]==x:
            return x
        
        return self.find(self.parent[x])
    def union(self,x,y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent > y_parent:
            self.parent[x_parent]=y_parent
        else:
            self.parent[y_parent]=x_parent
                
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dsu = UnionFind()
        res = ''

        for i in range(len(s1)):
            dsu.union(s1[i],s2[i])

       
        for i in range(len(baseStr)):
            parent = dsu.find(baseStr[i])
            res+=parent
        
        return res
