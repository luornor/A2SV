def solve():
    n = int(input())
    string = input()
    res = 0
    
    for i in range(n-2):
        if string[i]==string[i+1]==string[i+2]=='.':
            return 2
        elif string[i]=='.':
            res+=1
    if len(string)>=2 and string[-2]=='.':
        res+=1
    if string[-1]=='.':
        res+=1

    return res
        
            
        
t = int(input())
for _ in range(t):
    print(solve())