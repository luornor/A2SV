def solve(h,n):
    required = 0
    for i in range(n):
        required += i
        # If the total number of blocks so far is less than the required.
        if required > sum(h[:i+1]):  
            return 'NO'
    return 'YES'  
    

t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int,input().split()))
    print(solve(h,n))

