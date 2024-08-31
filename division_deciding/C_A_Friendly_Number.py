
n = int(input())
a = list(map(int, input().split()))

small = min(a)

check = all(num % small == 0 for num in a)

if check:
    print(small)
else:
    print(-1)