def numberOftimes(n):
    count = 0
    while n:
        count += 1
        n = n // 3
    return count

arr = [0] * (2 * 10**5+1)
for i in range(1, 2 * 10**5+1):
    arr[i] = arr[i - 1] + numberOftimes(i)

def solve():
    l, r = map(int, input().split())
    return  (arr[r] - arr[l-1]) + numberOftimes(l)


for _ in range(int(input())):
    print(solve())
