from collections import Counter
from math import factorial

int(input())
a = list(map(int, input().split()))

count = Counter(a)
unique = len(count)

print(factorial(unique))
