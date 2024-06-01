def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = a[0]
    for i in range(1, n):
        ans &= a[i]
    return ans

for _ in range(int(input())):
    print(solve())