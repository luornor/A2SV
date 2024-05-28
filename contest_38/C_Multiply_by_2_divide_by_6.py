def solve():
    n = int(input())
    if n==1:
        return 0
    count = 0
    while n!=1:
        if n%6==0:
            n/=6
            count+=1
        else:
            #check if u multiply by 2 it will work
            mult = n*2
            if mult%6==0:
                n*=2
                count+=1
            else:
                return -1
            
    return count


    
t = int(input())
for _ in range(t):
    print(solve())