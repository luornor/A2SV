MOD = 10**9 + 7

def generate_palindromes(limit):
    palindromes = []
    for num in range(1, limit + 1):
        if str(num) == str(num)[::-1]:
            palindromes.append(num)
    return palindromes


def solve():
    n = int(input())
    palindrome = generate_palindromes(n)
    dp = [0]*(n+1)
    dp[0] = 1

    for p in palindrome:
        for i in range(p,n+1):
            dp[i] = (dp[i]+ dp[i-p])%MOD

    return dp[n]

for _ in range(int(input())):
    print(solve())