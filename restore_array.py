"""
Kristina had an array a of length n consisting of non-negative integers.
She built a new array b of length n-1,such that bi=max(ai,ai+1)(1≤i≤n-1).

For example, suppose Kristina had an array a = [3,0,4,0,5] of length 5
Then she did the following:
Calculated b1=max(a1,a2)=max(3,0)=3;
Calculated b2=max(a2,a3)=max(0,4)=4;
Calculated b3=max(a3,a4)=max(4,0)=4;
Calculated b4=max(a4,a5)=max(0,5)=5.
As a result, she got an array b= [3,4,4,5] of length 4.
You only know the array b. 
Find any matching array a that Kristina may have originally had.
Input
The first line of input data contains a single integer t(1≤t≤104) — the number of test cases.
The description of the test cases follows.
The first line of each test case contains one integer n(2≤n≤2⋅105) —
the number of elements in the array a that Kristina originally had.
The second line of each test case contains exactly n-1
non-negative integer — elements of array b(0≤bi≤109).
Output
For each test case on a separate line, print exactly n
 non-negative integers — the elements of the array a
 that Kristina originally had.

If there are several possible answers — output any of them.
"""

t = int(input())

def solve():
    n = int(input())
    b = list(map(int, input().split()))
    # a0 = b[0]
    # an = b[-1]
    a = [0]*n
    
    a[0] = b[0]
    a[-1] = b[-1]
    for i in range(1,n-1):
        a[i]=min(b[i-1],b[i])
    print(*a)
        

for _ in range(t):
    solve()