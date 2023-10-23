from math import factorial
def solve(a,n):
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if a[i]<i+1<a[j]<j+1:
    #             count+=1
    pairs = []
    check = set()
    for i,num in enumerate(a):
        if i+1>num and num not in check:
            pairs.append((num,i+1))
            check.add(num)
    
    if len(pairs)>=2:
        count=int(factorial(len(pairs))/(factorial(2)*factorial(len(pairs)-2)))
    else:
        count=0

    pairs.sort()
    #check adjanc
    for i in range(len(pairs)-1):
        num,idx = pairs[i]
        if pairs[i+1][0]-pairs[i][0]==1:
            count-=1
        if idx in check and pairs[i+1][0]-pairs[i][0]!=1:
            count-=1

    
    print(count)
    


    

t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    solve(a,n)