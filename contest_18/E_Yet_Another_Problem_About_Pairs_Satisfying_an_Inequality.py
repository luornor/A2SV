from math import factorial
def solve(a,n):
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if a[i]<i+1<a[j]<j+1:
    #             count+=1
    count = 0
    valid_indexes = []

    for i in range(n):
        if a[i] >= i+1: continue
        # count of valid indexes that are less than a[i]
        count += 1
        valid_indexes.append(i+1)

    for j in range(n):
        if j < len(valid_indexes):
            if valid_indexes[j]<a[j]:
                count-=1
    print(count)
    print(valid_indexes)

    
    


    

t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    solve(a,n)