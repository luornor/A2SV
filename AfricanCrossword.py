"""
An African crossword is a rectangular table n x m in size. 
Each cell of the table contains exactly one letter. 
This table (it is also referred to as grid) contains some encrypted word that needs to be decoded.

To solve the crossword you should cross out all repeated letters in rows and columns.
In other words, a letter should only be crossed out if and only if
the corresponding column or row contains at least one more letter that is exactly the same.
Besides, all such letters are crossed out simultaneously.

When all repeated letters have been crossed out, we should write the remaining letters in a string.
The letters that occupy a higher position follow before the letters that occupy a lower position.
If the letters are located in one row, then the letter to the left goes first.
The resulting word is the answer to the problem.

You are suggested to solve an African crossword and print the word encrypted there.

Input
The first line contains two integers n and m (1≤n,m≤100).
Next n lines contain m lowercase Latin letters each. 
That is the crossword grid.

Output
Print the encrypted word on a single line. 
It is guaranteed that the answer consists of at least one letter.

"""
n,m = map(int,input().split())

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    new_mat = [[0] * rows for i in range(cols)]
        
    for col in range(cols):
        for row in range(rows):
                new_mat[col][row]=matrix[row][col]
    return new_mat

def solve(mat):
    rows = len(mat)
    cols = len(mat[0])
    for i in range(cols-1):
        for j in range(rows-1):
            if mat[j][i]==mat[j+1][i+1]:
                mat[j][i]=None
                mat[j+1][i+1]=None    
              
    column_grid = transpose(mat)
    
    for i in range(len(column_grid)-1):
        for j in range(len(column_grid[0])-1):
             if column_grid[i][j]==column_grid[i+1][j+1]:
                column_grid[i][j]=None
                column_grid[i+1][j+1] = None
    print(mat)            
    print(column_grid)


# grid= []
# for _ in range(n):
#     m = list(input())
#     grid.append(m)


print(solve([['c', 'b', 'a'], ['b', 'c', 'd'], ['c', 'b', 'c']]))
