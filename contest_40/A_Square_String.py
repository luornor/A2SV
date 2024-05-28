def solve():
    s = input()
    m = len(s)
    for i in range(1, m // 2 + 1):
        if 2*s[:i] == s:
            return "yes"
    return "no"


t = int(input())
for _ in range(t):
    print(solve())
    
