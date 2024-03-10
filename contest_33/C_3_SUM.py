def solve():
    n = int(input())
    a = list(map(int, input().split()))

    rem = []
    for i in range(n):
        if rem.count(a[i] % 10) < 3:  # Check if the count is less than 3 before appending
            rem.append(a[i] % 10)

    m = len(rem)
    
    for i in range(m):
        for j in range(i + 1, m):
            for k in range(j + 1, m):
                if (rem[i] + rem[j] + rem[k]) % 10 == 3:
                    return 'YES'
    return 'NO'

    



t = int(input())
for _ in range(t):
    print(solve())