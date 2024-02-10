t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    min_len = 0
    
    start=None
    end = None
    for i in range(n):
        if start is None and s[i]=='B':
            start=i
        
        if s[i]=='B':
            end=i

    print(end-start+1)


