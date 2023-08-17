"""
Considering an array a of n (n≥2) positive integers, 
the following inequality holds for 2≤i≤n: gcd(a1,a2,⋯,ai)≤gcd(a1,a2)≤2

Therefore, when the prefix [$a_1$,a2] of a is good, we can show that all the prefixes of a whose length
is no less than 2 are good, then a is beautiful. It is obvious that [a1,a2] 
is good when a is beautiful. So we get the conclusion that a is beautiful if and only if
the prefix [a1,$a_2$] is good.

We can check if there exist ai,aj(i≠j) such that gcd(ai,aj)≤2. If so, we can move ai,aj
to the front of a to make it beautiful, then the answer is Yes. If not, the answer is No.

Time complexity: O(n2log106)
"""
import math


def is_beautiful_prefix(a,n):
    for i in range(n):
        for j in range(i + 1, n):
            if math.gcd(a[i], a[j]) <= 2:
                return True
    return False


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    if is_beautiful_prefix(a,n):
        print('Yes')
    else:
        print('No')