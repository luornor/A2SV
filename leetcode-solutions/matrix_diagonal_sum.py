
# mat = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
grid = [[2,5,4],
        [1,5,1]]

# sum=0
# for i in range(len(mat)):
#     sum+=mat[i][i]
#     if i!= len(mat)-1-i:
#         sum+=mat[i][len(mat)-1-i]
# print(sum)
 

# print(grid[0][0])
# for i in range(rows):
#     for j in range(cols):
#         p_s[i][j]=grid[i][j]+p_s[i-1][j]+p_s[i][j-1]-p_s[i-1][j-1]
rows = len(grid)
cols = len(grid[0])
p_s = [[0]*(cols+1) for _ in range(rows+1)]
count = 0
for c in range(cols):
    count+=grid[0][c]
    for i in range(rows):
        p_s[i][0]=count

count = 0
for r in range(rows):
    count+=grid[r][1]
    for i in range(cols):
        p_s[0][i]=count

    
print(p_s)
        

            
                
            
            



 
