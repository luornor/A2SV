
# def merge(a,b):
#     arr = []
#     l = 0
#     r = 0
#     while l<len(a) and r<len(b):
#         if a[l]<b[r]:
#             arr.append(a[l])
#             l+=1
#         else:
#             arr.append(b[r])
#             r+=1

#     while l<len(a):
#         arr.append(a[l])
#         l+=1
    
#     while r<len(b):
#         arr.append(b[r])
#         r+=1

#     return arr



# def mergesort(arr):
#     if len(arr)<=1:
#         return arr
    
#     m=len(arr)//2
#     a = mergesort(arr[:m])
#     b = mergesort(arr[m:])
    

#     return merge(a,b)


# print(mergesort([4,5,1,2,6,3]))
import collections
def solveSudoku(board):
    """
    Do not return anything, modify board in-place instead.
    """
    #put number in memory
    sub_boxes = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    row_num = len(board)
    col_num = len(board[0])
    #Each row must contain the digits 1-9 without repetition.
    for row in range(row_num):
        for col in range(col_num):
            if board[row][col]!='.':
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                sub_boxes[(row//3,col//3)].add(board[row][col])

    def isValid(num,r,c):
            num=str(num)
            if  (num in rows[r] or
                num in cols[c] or 
                num in sub_boxes[(r//3,c//3)]):
                return False
            else:
                return True
    
        
    def solve(r,c):
        if r==row_num:
            return True
        #check for base cases
        if c==col_num:
            return solve(r+1,0)
        #how do we know we hv filled the entire board
        
        #if board is empty try to place number
        if board[r][c] != '.':
            return solve(r,c+1)
        #loop through all possible numbers
        for num in range(1,10):
            #if number is valid place it
            if isValid(num,r,c):
                board[r][c]=str(num)
                rows[r].add(str(num))
                cols[c].add(str(num))
                sub_boxes[(r//3,c//3)].add(str(num))
                #backtrack to next cell
                if solve(r,c+1):
                    return True
                #remove element if number is not valid
                board[r][c]='.'
                rows[r].remove(str(num))
                cols[c].remove(str(num))
                sub_boxes[(r // 3, c // 3)].remove(str(num))
        return False
        
    solve(0,0)

board = [[".","1",".","9",".","6",".",".","."],
        ["3",".","4","8",".",".",".",".","."],
        [".","6",".","4","7",".",".","9","."],
        ["1","2","3","6",".",".",".","7","9"],
        ["5",".","9",".",".","4","1",".","2"],
        [".",".","6","2","1",".",".",".","8"],
        ["6",".",".",".","9",".","2","5","."],
        [".",".","1",".","4","2","6","8","."],
        ["4",".","2","5",".",".",".",".","3"]]


board1= [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]


            
solveSudoku(board)
print(board)



        