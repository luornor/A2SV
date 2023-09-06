def solve(n):
    a =[]
    
    
    for i in range(1, n + 1):
        a.append(2*i)
    
    print(*a)



t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)