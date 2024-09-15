from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a_count = Counter(a)
    max_count = max(a_count.values())
    print(max_count)