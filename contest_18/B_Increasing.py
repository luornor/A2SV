def solve(a, n):
    a.sort()
    for i in range(1, n):
        if a[i] <= a[i - 1]:
            return 'NO'
    return 'YES'

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a, n))
