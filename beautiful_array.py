"""Vitaly has an array of n distinct integers. Vitaly wants to divide this array into three non-empty sets
so as the following conditions hold:

The product of all numbers in the first set is less than zero (<0).
The product of all numbers in the second set is greater than zero (>0).
The product of all numbers in the third set is equal to zero.
Each number from the initial array must occur in exactly one set."""

def check_product(list1,val):
    product = 1
    for item in list1:
        product *=item
    if product > 0:
        list1.remove(val)
        return True

def solve(elements):
    set1 = {1}
    set2 = {1}
    set3 = {1}
    for i in range(n):
        if elements[i]==0:
            set3.add(elements[i])
        elif elements[i]>0:
            set2.add(elements[i])
        elif elements[i]<0:
            set1.add(elements[i])
            if check_product(set1,elements[i]):
                set2.add(elements[i])

    print(*set1)
    print(*set2)
    print(*set3)


n = int(input())

elements = list(map(int,input().split()))
solve(elements)

