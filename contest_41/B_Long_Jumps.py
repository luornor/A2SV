
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    dp = [0] *(n+1)

    for i in range(n,0,-1):
        if a[i-1]+i>n:
            dp[i] = a[i-1]
        else:
            dp[i] = a[i-1] + dp[i + a[i-1]]


    print(max(dp))
