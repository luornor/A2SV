def solve():
    n = int(input())
    s = input()
    count = 0
    
    for i in range(n-2):
        if s[i]==s[i+1]==s[i+2]=='.':
            return 2
        elif s[i]=='.':
            count+=1
    if len(s)>=2 and s[-2]=='.':
        count+=1
    if s[-1]=='.':
        count+=1

    return count
        
            
        
t = int(input())
for _ in range(t):
    print(solve())