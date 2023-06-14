"""
An array b of m
positive integers is good if for all pairs i and j (1≤i,j≤m),
max(bi,bj) is divisible by min(bi,bj)
You are given an array a of n positive integers. 
You can perform the following operation:

Select an index i (1≤i≤n) and an integer x
(0≤x≤ai) and add x to ai in other words, ai:=ai+x
After this operation, ai ≤ 10^18should be satisfied.
You have to construct a sequence of at most n
operations that will make a good.
It can be proven that under the constraints of the problem,
 such a sequence of operations always exists.
"""
N=int(input())
import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        val = nearest_power_of_two(a[i])
        x = (val - a[i]) 
        print(i + 1,x)

def nearest_power_of_two(num):
    return num**2


for i in range(N):
    solve()
