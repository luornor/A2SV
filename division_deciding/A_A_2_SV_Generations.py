n = int(input())
a = list(map(int, input().split()))

a.sort()

median = n//2
print(a[median])