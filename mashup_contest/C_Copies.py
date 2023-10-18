def solve(n,x,y):
    min_time=0
    if x<=y:
        min_time=(n-1)*x

    else:
        min_time=(n-1)*y
        
        
    print(min_time)


n,x,y=map(int,input().split())
solve(n,x,y)