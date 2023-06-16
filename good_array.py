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
N=int(input())

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
