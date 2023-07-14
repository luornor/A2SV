
mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]

sum=0
for i in range(len(mat)):
    sum+=mat[i][i]
    if i!= len(mat)-1-i:
        sum+=mat[i][len(mat)-1-i]
           
            
                
            
            




    
    
        
    
        





        
print(sum)
