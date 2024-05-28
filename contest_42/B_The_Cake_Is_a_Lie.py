def solve():
    n,m,k = map(int,input().split())

    total_cost = n*m-1
    if total_cost==k:
        return 'YES'
    else:
        return 'NO'


for _ in range(int(input())):
    print(solve())