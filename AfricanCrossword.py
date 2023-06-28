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
rows,cols = map(int,input().split())

matrix = [input() for _ in range(rows)]

def crosswordSolve(grid,rows,cols):
    # create a boolean grid to mark repeated letters in grid
    cross_out = [[False for _ in range(cols)] for _ in range(rows)]
    #for rows
    # keep of track of counts of each letter for a row
    for r in range(rows):
        row_counts = {}
        for c in range(cols):
            current = grid[r][c]
            row_counts[current] = row_counts.get(current,0)+1

        # check if letter appears more than once in a row 
        # and mark its position in the cross_out  grid as True if it does
        for c in range(cols):
            if row_counts[grid[r][c]] > 1:
                cross_out[r][c]=True
    #For columns
    #keep track of counts of each letter in a column
    for c in range(cols):
        col_counts = {}
        for r in range(rows):
            current = grid[r][c]
            col_counts[current]=col_counts.get(current,0)+1

        # check if letter appears more than once in a column 
        # and mark its position in the cross_out grid as True If it does 
        for r in range(rows):
            letter = grid[r][c]
            if col_counts[letter]>1:
                cross_out[r][c]=True

    #create the encrypted word
    encrypted_word = ""
    for r in range(rows):
        for c in range(cols):
            if not cross_out[r][c]:
                encrypted_word+= grid[r][c]

    return encrypted_word
    
print(crosswordSolve(matrix,rows,cols))
