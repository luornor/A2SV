def solve(a, n):
    count = 0
    max_count = 0
    #max count of consecutive zeros
    for num in a:
        if num == 0:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    print(max_count)





t = int(input())
for _ in range(t):
    n=int(input())
    a = list(map(int,input().split()))
    solve(a,n)