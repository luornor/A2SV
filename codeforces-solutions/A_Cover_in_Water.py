def solve():
    n = int(input())
    s = input()
    res = 0
    
    for i in range(n-2):
        if s[i]==s[i+1]==s[i+2]=='.':
            return 2
        elif s[i]=='.':
            res+=1
    if len(s)>=2 and s[-2]=='.':
        res+=1
    if s[-1]=='.':
        res+=1

    return res
        
            
        
t = int(input())
for _ in range(t):
    print(solve())