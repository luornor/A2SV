"""Vitaly has an array of n distinct integers. Vitaly wants to divide this array into three non-empty sets
so as the following conditions hold:

The product of all numbers in the first set is less than zero (<0).
The product of all numbers in the second set is greater than zero (>0).
The product of all numbers in the third set is equal to zero.
Each number from the initial array must occur in exactly one set."""

n = int(input())
set1 = set()
set2 = set()
set3 = set()

elements = list(map(int,input().split()))

for i in range(n):
    if elements[i]<0:
        set1.add(elements[i])
    elif elements[i]>0:
        set2.add(elements[i])
    else:
        set3.add(elements[i])

print(*set1)
print(*set2)
print(*set3)
