def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort(reverse=True)
    if a[0]>=x:
        return 2
    else:
        sum = a[0]
        i = 1
        while i < n and sum < x:
            sum += a[i]
            i += 1
        if sum < x:
            return sum
        # elif sum == x:
        #     return i*2
        else:
            return (i-1) + 3

t = int(input())
for _ in range(t):
    print(solve())