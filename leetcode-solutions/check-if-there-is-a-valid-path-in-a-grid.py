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

    
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        connections  = {
            1: [(0,-1),(0,1)], # left cell and the right cell
            2: [(-1,0),(1,0)], # upper cell and the lower cell.
            3: [(0,-1),(1,0)], # left cell and the lower cell
            4: [(0,1),(1,0)], # right cell and the lower cell
            5: [(0,-1),(-1,0)], # left cell and the upper cell.
            6: [(0,1),(-1,0)] # right cell and the upper cell.
        }

        def inbound(a,b,i,j):
            street = grid[i][j]
            if i+1<m:
                if grid[i+1][j]==2 and street==6:
                    return False
            valid_paths ={
                    1: {1,3,5},
                    2: {2,5,6},
                    3: {2,5,6},
                    4: {2,3,5,1,6},
                    5: {},
                    6: {2,5,3,4,1},
                }

            if 0<= a <m and 0<= b <n:
                if grid[a][b] in valid_paths[street]:
                    return True

            return False

        dsu = UnionFind(m*n)
        for i in range(m):
            for j in range(n):
                for x,y in connections[grid[i][j]]:
                    a,b = i+x , j+y
                    if inbound(a,b,i,j):
                        #how to represent (i,j) as one index
                        dsu.union(i*n+j,a*n+b)
        
        
        return dsu.find(0)==dsu.find(m*n-1)
