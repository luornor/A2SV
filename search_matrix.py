def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    row=0
    col=0
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    while row <num_rows:
        while col< num_cols:
            if target==matrix[row][col]:
                return True
            col+=1
        col=0
        row+=1






















# O(log(m*n)) implementation
# def searchMatrix(matrix, target):
#     if not matrix or not matrix[0]:
#         return False

#     num_rows = len(matrix)
#     num_cols = len(matrix[0])
#     left = 0
#     right = num_rows * num_cols - 1

#     while left <= right:
#         mid = (left + right) // 2
#         mid_element = matrix[mid // num_cols][mid % num_cols]

#         if mid_element == target:
#             return True
#         elif mid_element < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return False


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))