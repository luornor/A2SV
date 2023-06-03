
n = int(input())

def solve(s):
    x = s.split('#')
    print(*x)

ans = [input() for _ in range(n)]

for item in ans:
    solve(item)
    