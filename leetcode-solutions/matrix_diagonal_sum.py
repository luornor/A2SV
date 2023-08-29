
mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]

sum=0
for i in range(len(mat)):
    sum+=mat[i][i]
    if i!= len(mat)-1-i:
        sum+=mat[i][len(mat)-1-i]
# print(sum)
 
cols = len(mat[0])
rows = len(mat[0])
p_s = [[0]*(cols+1) for _ in range(rows+1)]

# p_s[0][0] = mat[0][0]

# for i in range(1,rows):
#     p_s[i][0]=mat[i][0]+p_s[i-1][0]
# for j in range(1,cols):
#     p_s[0][j] += mat[0][j]+p_s[0][j-1]
for i in range(rows):
    for j in range(cols):
        p_s[i][j]=p_s[i-1][j]+p_s[i][j-1]-p_s[i-1][j-1]+mat[i][j]
    
        



print(p_s)
        

            
                
            
            



 
