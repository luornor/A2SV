def solve():
    n = int(input())
    a = list(map(int,input().split()))

    if min(a)==a[0]:
        return 'Bob'
    else:
        return 'Alice'
t = int(input())
for _ in range(t):
    print(solve())