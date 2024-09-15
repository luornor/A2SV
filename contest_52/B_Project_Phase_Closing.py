n, m ,k= map(int, input().split())

grid = []
for i in range(n):
    temp = []
    for j in range(m):
        left = (i * m + j) * 2 + 1
        right = left + 1
        if left==k:
            print(i+1,j+1,'L')
        if right==k:
            print(i+1,j+1,'R')
            
# temp.append((left, right))
# grid.append(temp)
