def solve():
    s = input()
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 1
    MOD = 10**9 + 7
    if 'm' in s or 'w' in s:
        return 0
    for i in range(2, len(s) + 1):
        if s[i-1] + s[i-2] == 'uu' or s[i-1] + s[i-2] == 'nn':
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
        else:
            dp[i] = dp[i-1]
    # print(dp)
    return dp[len(s)]

print(solve())
