class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        def is_valid(r,c):
            return r<len(mat) and c<len(mat[0]) and r>=0 and c>=0

        grid = [[0]*len(mat[0]) for _ in range(len(mat))]

        queue = deque()
        visited = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    queue.append(((i,j),0))
                    visited.add((i,j))

        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        while queue:
            (r,c),step = queue.popleft()
            
            grid[r][c]=step
            
            for x,y in directions:
                new_r = r+x
                new_c = c+y

                if is_valid(new_r,new_c) and (new_r,new_c) not in visited :
                    queue.append(((new_r,new_c),step+1))
                    visited.add((new_r,new_c))


        return grid
        