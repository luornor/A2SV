n = int(input())
juices = []
for _ in range(n):
    c, s = input().split()
    price = int(c)
    vitamins = sum(1 << (ord(vitamin) - ord('A')) for vitamin in s)
    juices.append((price, vitamins))

#juices contain the vitamins represented as a number

dp = [float('inf')] * 8
dp[0] = 0
for price, vitamins in juices:
    
    for mask in range(7):
        new_mask = mask | vitamins
        dp[new_mask] = min(dp[new_mask], dp[mask] + price)
        # print(dp)


if dp[7] == float('inf'):
    print(-1)
else:
    print(dp[7])