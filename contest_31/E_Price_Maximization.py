def solve():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))

    a.sort()

    left = 0
    right = n - 1
    total_cost = 0

    while left < right:
        weight = a[left] + a[right]
        total_cost += weight // k
        left += 1
        right -= 1

    return total_cost
    

t = int(input())
for _ in range(t):
    print(solve())