t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    even_count = 0
    odd_count = 0
    total = sum(a)
    for num in a:
        if num%2==0:
            even_count+=1
        else:
            odd_count+=1

    for _ in range(q):
        type,num = map(int,input().split())
        #even increments
        
        if type==0:
            total+=(num*even_count)

            #even+odd=odd
            if num%2!=0:
                odd_count+=even_count
                even_count=0
        else:
            total+=(num*odd_count)

            #odd+odd=even
            if num%2!=0:
                even_count+=odd_count
                odd_count=0
    
        print(total)
