MOD = 998244353

def calculate_score(n, arr):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        dp[i] = (dp[i - 1] * 2) % MOD
    
    ans = 0
    for i in range(n):
        cnt = dp[n - i] - 1
        ans = (ans + arr[i] * cnt) % MOD
    
    return ans

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Calculate and output the result
result = calculate_score(n, arr)
print(result)
