def solve():
    n = int(input())
    a = list(map(int,input().split()))

    even = 0
    for num in a:
        if num%2==0:
            even+=1
    odd = n-even

    for i in range(0,n,2):
        a[i]+=1
    
    even_after = 0
    for num in a:
        if num%2==0:
            even_after+=1
    
    odd_after =n-even_after

    if even==n or odd==n or even_after==n or odd_after==n:
        return 'YES'
    else:
        return 'NO'



t = int(input())
for _ in range(t):
    print(solve())