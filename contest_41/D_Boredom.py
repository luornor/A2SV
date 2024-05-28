
n = int(input())
a = list(map(int,input().split()))

n = max(a)
hmap = [0]*(n+1)
for num in a:
    hmap[num]+=num

dp = [0]*(n+1)
dp[1] = hmap[1]
for i in range(2,n+1):
    dp[i] = max(dp[i-2]+hmap[i],dp[i-1])

print(dp[-1])