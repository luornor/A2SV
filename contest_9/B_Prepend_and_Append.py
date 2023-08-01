def solve(n,s):
    if not s:
        print(0)
    
    l = 0
    r = n-1
    res = n
    while l<=r:
        if (s[l]=='0' and s[r]=='1') or (s[l]=='1' and s[r]=='0'):
            res-=2
            l+=1
            r-=1
        else:
            print(res)
            return

    print(res)

    
    # l = 0
    # res = 0
    # while l<n//2:
    #     if s[l]==s[n-l-1]:
    #         res=n-2*l
    #         break
    #     l+=1

    # if res==0 and n%2==1:
    #     return 1
    # else:
    #     return res
       
    
    





t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    solve(n,s)
