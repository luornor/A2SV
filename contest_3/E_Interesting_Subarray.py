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

   for i in range(n):
        min_a = a[i]
        max_a = a[i]
        for j in range(i+1,n):
            min_a = min(min_a,a[j])
            max_a = max(max_a,a[j])
            if max_a-min_a>=2:
                print('YES')
                print(i+1,j+1)
                break
            else:
                continue
        break
   else:
       print('NO')
           

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    solve(n,a)


t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Length of the array
    a = list(map(int, input().split()))  # Elements of the array
    
    max_diff = -1
    max_diff_index = -1

    for i in range(n):
        if a[i] > max_diff:
            max_diff = a[i]
            max_diff_index = i

    if max_diff_index == 0 or max_diff_index == n - 1:
        print("NO")
    else:
        print("YES")
        print(max_diff_index, max_diff_index + 1)
