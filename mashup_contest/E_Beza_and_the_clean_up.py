n, m, s, A, B = map(int, input().split())
values_a = list(map(int, input().split()))
values_b = list(map(int, input().split()))

max_total_cost = 0

for a_count in range(n+1):
    remaining_weight = s - (a_count * A)
    if remaining_weight >= 0:
        b_count = min(remaining_weight // B, m)
        total_cost = sum(values_a[:a_count]) * A + sum(values_b[:b_count]) * B
        max_total_cost = max(max_total_cost, total_cost)

print(max_total_cost)