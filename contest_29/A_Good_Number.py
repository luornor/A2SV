n, k = map(int, input().split())
count = 0

for _ in range(n):
    a = input()
    unique = set()

    for num in a:
        if 0<= int(num) <= k:
            unique.add(int(num))

    if len(unique) == k + 1:
        count += 1

print(count)
