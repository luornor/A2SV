class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        e_r,e_c = entrance
        queue = deque([(e_r, e_c, 0)])
        visited = set([(e_r, e_c)])
        def is_valid(r,c):
            return 0<= r <len(maze) and 0<= c <len(maze[0])
        # print(queue)
        while queue:
            r,c,step = queue.popleft()
            #empty cell that is at the border of the maze
            if (
            (r!=e_r or c!=e_c)
            and (r==0 or r==len(maze)-1 or c==0 or c==len(maze[0])-1)):
                return step

            for x,y in directions:
                new_r = x+r
                new_c = y+c
                if (
                    is_valid(new_r,new_c) 
                and (new_r,new_c) not in visited 
                and maze[new_r][new_c]!='+'):
                    queue.append((new_r,new_c,step+1))
                    visited.add((new_r, new_c))

        return -1

        