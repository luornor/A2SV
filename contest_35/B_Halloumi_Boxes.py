
def solve():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    
    if sorted(a)==a or k>1: 
        return 'YES'
    else:
        return 'NO'
    

t = int(input())
for _ in range(t):
    print(solve())