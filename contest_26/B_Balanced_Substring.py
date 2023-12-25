def solve():
    n = int(input())
    s = input()
    for i in range(n - 1):
        if s[i] != s[i + 1]: 
            return [i + 1, i + 2]
    return [-1, -1]


t = int(input())
for _ in range(t):
    print(*solve())