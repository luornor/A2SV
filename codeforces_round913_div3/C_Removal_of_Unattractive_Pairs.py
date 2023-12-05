def solve():
    n = int(input())
    s = input()
    s = list(s)
    res = n
    l = 0
    r = 1
    while r< n-1:
        if s[l]!=s[r]:
            l+=1
            r+=1
        else:
            r+=1
            
    return n-(r-l+1)




t = int(input())
for _ in range(t):
    print(solve())