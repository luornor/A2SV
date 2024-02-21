def solve():
    n = int(input())
    grid = []

    for _ in range(n):
        grid.append(input())

    arr = [row.count('1') for row in grid]

    check = [num for num in arr if num!=0]
    
    # print(chek)
    return 'TRIANGLE' if len(set(check)) == len(check) else 'SQUARE'

t = int(input())
for _ in range(t):
    print(solve())