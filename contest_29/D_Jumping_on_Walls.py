n,k = map(int, input().split())

left_wall = input()
right_wall = input()

area = 0
for i in range(n):
    if left_wall[i]=='-':
        area+=1
    else:
        idx = i+k
        if idx<n and right_wall[idx]=='-':
            area+=k
        else:
            break

if area>=n:
    print('YES')
else:
    print('NO')
