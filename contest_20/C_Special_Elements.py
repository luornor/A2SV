def count_special_elements(n, a):
    prefix = [0] * (n + 1)
    prefix[1] = a[0]

    for i in range(2, n + 1):
        prefix[i] = prefix[i - 1] + a[i - 1]

    special_count = 0

    for i in range(n-1):
        for j in range(i + 2, n +1):
            if prefix[j] - prefix[i] in a:
                special_count += 1

    return special_count


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    special_count = count_special_elements(n, a)

    print(special_count)