from math import gcd
n= int(input())
a = list(map(int,input().split()))

dp = [1]*(n+1)

for i in range(n):
    for j in range(i+1,n):
        if gcd(a[i],a[j])>1:
            dp[j] = max(dp[j],dp[i]+1)

print(max(dp))
