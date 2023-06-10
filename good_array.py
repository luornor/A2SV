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

def solve(a,n):
    p = 0
    i = 1
    x = a[0]
    res = []
    while i<=n:
        a[i] = a[i]+x
        p+=1
        i+=1
        res.append([i,x])
    print(p)
    for i in range(p):
        print(*res[i])
    

for _ in range(N):
    n = int(input()) 
    a = list(map(int,input().split()))
    solve(a,n)