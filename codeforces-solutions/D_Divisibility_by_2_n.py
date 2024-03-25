def solve():
    n = int(input())
    a = list(map(int,input().split()))

    count_two = sum(1 for num in a if num%2==0)
    
    if count_two>=n:
        return 0
    
    

    operations = 0
    for num in a:
        while num % 2 ==0 and count_two<n:
            num*=2
            count_two+=1
            operations+=1

        if count_two>=n:
            break
        
    if count_two>=n:
        return operations
    else:
        return -1
    

t = int(input())
for _ in range(t):
    print(solve())
