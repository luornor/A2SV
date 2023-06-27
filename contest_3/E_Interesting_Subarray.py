"""
For an array a of integers let's denote its maximal element as max(a), and minimal as min(a)
We will call an array a of k integers interesting if max(a)-min(a)≥k.
For example, array [1,3,4,3] isn't interesting as max(a)-min(a)=4-1=3<4
while array [7,3,0,4,3] is as max(a)-min(a)=7-0=7≥5.

You are given an array a of n integers. Find some interesting nonempty subarray of a,
or tell that it doesn't exist.

An array b is a subarray of an array a if b can be obtained from a
by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) 
elements from the end. In particular, an array is a subarray of itself.

Input
The first line contains integer number t(1≤t≤10000). Then t test cases follow.

The first line of each test case contains a single integer n (2≤n≤2⋅105) — the length of the array.

The second line of each test case contains n integers a1,a2,…,an (0≤ai≤109) — the elements of the array.

It is guaranteed that the sum of n
over all test cases does not exceed 2⋅10^5.

Output
For each test case, output "NO" in a separate line if there is no interesting nonempty subarray in a.

Otherwise, output "YES" in a separate line. In the next line, output two integers l and r
(1≤l≤r≤n) — bounds of the chosen subarray. If there are multiple answers, print any.

You can print each letter in any case (upper or lower).
"""
t = int(input())

def solve(n,a):
    p = 0
    for i in range(1,n):
        if abs(a[i]-a[i-1])>=2:
            print('YES')
            print(i,i+1)
            p = 1
            break

    if p==0:
        print('NO')

           

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    solve(n,a)

