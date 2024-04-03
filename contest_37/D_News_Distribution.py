class UnionFind:
    def __init__(self,n):
        self.parent = {i:i for i in range(n)}
        self.size = [1]*n
    
    def find(self,x):
        if self.parent[x]==x:
            return x
        
        return self.find(self.parent[x])
    
    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]


def solve():
    n, m = map(int, input().split())
    dsu = UnionFind(n)
    for i in range(m):
        group = list(map(int, input().split()))[1:]
        for i in range(1,len(group)):
            dsu.union(group[0]-1,group[i]-1)

    res = []
    
    for i in range(n):
        res.append(dsu.size[dsu.find(i)])

    return res

print(*solve())



