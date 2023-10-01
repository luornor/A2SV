def can(k, v, h):
    res = 0
    for i in range(len(v) - 1):
        res += min(k, v[i + 1] - v[i])
    res += k
    return res >= h

t = int(input())

for _ in range(t):
    n, h = map(int, input().split())
    v = list(map(int, input().split()))
    left, right = 1, 10**18
    res = -1

    while left <= right:
        mid = left + (right - left) // 2
        if can(mid, v, h):
            res = mid
            right = mid - 1
        else:
            left = mid + 1

    print(res)
