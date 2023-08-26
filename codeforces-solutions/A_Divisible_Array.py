def solve(n):
    N = 2000001
    s = 0
    a = [0]*(N+1)
    for i in range(n, 1, -1):
        a[i] = i
        s = (s + i) % n
    a[1] = n - s
    
    
    for i in range(1, n + 1):
        print(a[i], end=' ')
    print()



t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)