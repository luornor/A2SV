t = int(input())

for _ in range(t):
    n = int(input())
    
    arr = [2,3,1]
    n-=6
    while n >= 3:
        arr[0]+=1
        arr[1]+=1
        arr[2]+=1
        n-=3
    if n==1:
        arr[1]+=1
    elif n==2:
        arr[0]+=1
        arr[1]+=1

    
    print(*arr)
   