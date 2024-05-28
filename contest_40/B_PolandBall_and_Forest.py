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


n = int(input())
p = list(map(int, input().split()))

dsu = UnionFind(n+1)
for i in range(1,n+1):
    dsu.union(i,p[i-1])

count = set()

for i in range(1,n+1):
    count.add(dsu.find(i))

print(len(count))

