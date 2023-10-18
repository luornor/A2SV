t = int(input())

for _ in range(t):
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    total_cost = p * n

    residents = sorted(zip(a, b), reverse=True)

    for i in range(1, n):
        cost = residents[i][1]
        if cost <= p:
            total_cost += cost
        else:
            total_cost += p

    print(total_cost)