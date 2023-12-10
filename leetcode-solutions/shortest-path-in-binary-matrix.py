class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1

        if len(grid)==1 and grid[0][0]==0:
            return 1

        queue = deque([((0,0),1)])
        visited = set((0,0))

        while queue:
            (r,c),path = queue.popleft()
            
            #visit neis
            nei = [(0,1),(0,-1),(1,0),(-1,0),
                        (1,1),(-1,-1),(1,-1),(-1,1)]

            for x,y in nei:
                new_r = r+x
                new_c = c+y

                if new_r<len(grid) and new_c<len(grid[0]) and new_r>=0 and new_c>=0 and grid[new_r][new_c]==0 and (new_r,new_c) not in visited :
                    queue.append(((new_r,new_c),path+1))
                    visited.add((new_r,new_c))
                    
                    if new_r==len(grid)-1 and new_c==len(grid[0])-1:
                        return path+1

        return -1
    

        
            

        
        