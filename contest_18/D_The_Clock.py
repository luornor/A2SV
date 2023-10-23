def solve(clock,x):
    x = int(x)



t = int(input())

for _ in range(t):
    clock,x=map(input().split())
    solve(clock,x)
