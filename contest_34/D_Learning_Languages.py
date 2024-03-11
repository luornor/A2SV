from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if self.size[root_x] < self.size[root_y]:
            root_x,root_y = root_y,root_x
        
        self.parent[root_x]=root_y
        

def solve():
    n, m = map(int, input().split())

    count=0
    dsu = UnionFind(n)
    visited = set()
    for _ in range(n):
        languages = list(map(int, input().split()))[1:]
        if not languages:
            count+=1
        else:
            for i in range(len(languages)-1):
                u = languages[i]-1
                visited.add(u)
                v = languages[i+1]-1
                dsu.union(u,v)
            visited.add(languages[-1]-1)

    #number of unique references
    unique = 0
    for i in range(len(dsu.parent)):
        if i in visited and dsu.find(i)==i:
            unique+=1
            

    return count+unique-1 if visited else count
        

print(solve())

