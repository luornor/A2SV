n, p = map(int, input().split())
positivity = list(map(int, input().split()))

def check(mid):
    total_positivity = sum(positivity[:mid])
    for i in range(mid, n):
        total_positivity += positivity[i] - positivity[i - mid]
        if total_positivity >= p:
            return True
    return False

left, right = 1, n
result = (-1, -1)

while left <= right:
    mid = (left + right) // 2
    if check(mid):
        result = (mid, right - mid + 1)
        right = mid - 1
    else:
        left = mid + 1

print(*result)
