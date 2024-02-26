
def solve():
    n =int(input())
    a = list(map(int,input().split()))
    dp = [0]*(n+1)

    for i in range(n,0,-1):
        if i +a[i-1]> n:
            dp[i]=a[i-1]
        else:
            dp[i] = a[i-1] + dp[i + a[i-1]]
    # print(dp)
    return max(dp)



t = int(input())
for _ in range(t):
    print(solve())
        