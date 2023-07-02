from collections import Counter, defaultdict


t = int(input())

def solve(l,n):
    #if 2 robots say that there are 2 robots infront 
    #at least one must say 1 robots are in front or 0 robots infront
    #count the number of appearances of each number
    #check if the count of number x is less than or equal number x-1
    # Problem A: 
    # 1: Count the number of occurances of each number in the array
    # 2: Check if the count of number x is less than or equals to the count of (x-1) for all unique x in the array
    
    # count = [0]*(max(l)+1) 
    # for i in range(n):
    #     count[l[i]] +=1
    # for i in range(1,len(count)):
    #     if count[i-1]<count[i]:
    #         return 'NO'
    # return 'YES' 
    a = [0] * n
    for i in range(n):
        a[i] = l[i]

    a.sort()

    for i in range(n):
        a[i] = i

    possible = True
    for i in range(n):
        if a[i] > i:
            possible = False
            break
    
    if possible:
        print("YES")
    else:
        print("NO")

    
    
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    solve(l,n)
       
