"""
An array b of m
positive integers is good if for all pairs i and j (1≤i,j≤m),
max(bi,bj) is divisible by min(bi,bj)
You are given an array a of n positive integers. 
You can perform the following operation:

Select an index i (1≤i≤n) and an integer x
(0≤x≤ai) and add x to ai in other words, ai:=ai+x
After this operation, ai ≤ 10^18 should be satisfied.
You have to construct a sequence of at most n
operations that will make a good.
It can be proven that under the constraints of the problem,
such a sequence of operations always exists.
Input
Each test contains multiple test cases. The first line contains a single integer t(1≤t≤104) — the number of test cases. 
The description of the test cases follows.

The first line of each test case contains a single integer n(1≤n≤10^5) — the length of the array a.

The second line of each test case contains n space-separated integers a1,a2,…,an(1≤ai≤109) — representing the array a.

Output
For each test, output a single integer p(0≤p≤n) — denoting the number of operations in your solution.

In each of the following p lines, output two space-separated integers — i and x.

You do not need to minimize the number of operations. It can be proven that a solution always exists.
"""
import math
N=int(input())

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a_copy = a.copy()

    # sort the array in non-decreasing order
    a.sort()

    # construct a good array
    operations = []
    for i in range(1, n):
        idx = a_copy.index(a[i])
        x = (a[i - 1] - (a[i] % a[i - 1])) % a[i - 1]
        a[i] += x
        operations.append((idx+1, x))
        a_copy[idx] = -1

    # output the number of operations and the operations themselves
    print(len(operations))
    for op in operations:
        print(op[0], op[1])

for i in range(N):
    solve()


# for _ in range(int(input())):
#     n = int(input())
#     data = list(map(int, input().split()))
#     data_copy = data.copy()
#     operations = []
#     data.sort()
#     for i in range(1,n):
#         idx = data_copy.index(data[i])
#         remainder = (data[i-1] -(data[i]%data[i-1]) )% data[i-1] 
#         data[i] += remainder 
#         if remainder:
#             operations.append((idx+1, remainder))
#         data_copy[idx] = -1
#     print(len(operations))
#     for i in sorted(operations, key= lambda x: x[0]):
#         print(*i)