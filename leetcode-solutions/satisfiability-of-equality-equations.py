class UnionFind:
    def __init__(self):
        self.parent = {c:c for c in list(string.ascii_lowercase)}
    
    def find(self,x):
        if self.parent[x]==x:
            return x

        return self.find(self.parent[x])
    
    def union(self,x,y):
        parent_x=self.find(x)
        parent_y=self.find(y)

        if parent_x > parent_y:
            self.parent[parent_x]=parent_y
        else:
            self.parent[parent_y]=parent_x

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        dsu = UnionFind()

        not_equal = []
        for item in equations:
            if item[1]==item[2]:
                dsu.union(item[0],item[3])
            else:
                not_equal.append([item[0],item[3]])
                    
        for item in not_equal:
            if dsu.find(item[0])==dsu.find(item[1]):
                return False
        
        return True
        

