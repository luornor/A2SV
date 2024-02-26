from collections import Counter

def solve():
    n = int(input())
    a = list(map(int,input().split()))
    s = input()

    #brute force
    # count = Counter(s)
    # check = set('abcdefghijklmnopqrstuvwxyz')
    # j = 0
    # for c in s:
    #     i = 0
        
    #     if a[j] not in check:
    #         chosen = a[j]
    #     while i<n:
    #         if a[i]==chosen:
    #             a[i]=c
    #             count[c]-=1

    #         if count[c]==0:
    #             del count[c]
    #         i+=1
        
    #     j+=1

  
    # if ''.join(a)== s:
    #     return 'YES'
    # else:
    #     return 'NO'
    #better
    hmap  = {}
    possible = True
    for i in range(n):
        if a[i] not in hmap:
            hmap[a[i]]=s[i]
        elif hmap[a[i]] != s[i]:
                possible=False
                break

    if possible:
        return 'YES'
    else:
        return 'NO'


    
t = int(input())
for i in range(t):
    print(solve())
        
        
         