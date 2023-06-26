"""
You are given a sequence of positive integers a1, a2, ..., an. Find all such indices i, 
that the i-th element equals the arithmetic mean of all other elements 
(that is all elements except for this one).

Input
The first line contains the integer n (2≤n≤2·10^5).
The second line contains elements of the sequence a1,a2,...,an (1≤ai≤1000).
All the elements are positive integers.
"""

n = int(input())
def solve(a):
    n = len(a)
    num_sum = sum(a)
    idx = []
    for  i in range(n): 
        avg = (num_sum-a[i])/(n-1)
        check(avg,a[i],i,idx)
    
    if idx:
        print(len(idx))
        for i,val in enumerate(idx):
            print(val, end=' ')
    else:
        print(0)
        print(' ')
    
def check(avg,num,i,idx):
    tolerance = 1e-9 
    if abs(avg - num) <= tolerance:
        idx.append(i + 1)

a = list(map(int, input().split()))
solve(a)