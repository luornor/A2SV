class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # rows = len(grid)
        # cols = len(grid[0])
        # ps = [[0]*(cols+1) for _ in range(3)]

        # for i in range(rows):
        #     for j in range(cols):
        #         ps[i][j]=ps[i-1][j]+ps[i][j-1]-ps[i-1][j-1]+grid[i][j]

        # print(ps)
        top_prefix = sum(grid[0])  #ps[0][-2]
        down_prefix = 0
        res = float('inf')
        for i in range(len(grid[0])):
            top_prefix-=grid[0][i]
            #first robot
            diff = max(top_prefix,down_prefix)
            #second robot
            res = min(res,diff)
            down_prefix+=grid[1][i]

            

        return res

