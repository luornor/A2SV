def solve():
    a,b,c = map(int,input().split())
    
    return 'YES' if a+b==c or a+c==b or b+c==a else 'NO'
        
t = int(input())
for _ in range(t):
    print(solve())
        