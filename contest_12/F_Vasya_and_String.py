def solve(n,k,s):
    a = 0
    l, r = 0, 0
    max_count = 0

    while r < n:
        if s[r] == 'a':
            a += 1
        if a <= k:
            max_count = max(max_count, r-l+1)
        while a>k:
            if s[l]=='a':
                a-=1
                l+=1
        r += 1

    l,r = 0,0
    b = 0
    while r<n:
        if s[r]=='b':
            b+=1
        if b<=k:
            max_count = max(max_count,r-l+1)
        while b>k:
            if s[l]=='b':
                b-=1
                l+=1
        r+=1


    print(max_count)
    




n,k = map(int,input().split())
s = input()
solve(n,k,s)
