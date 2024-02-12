def solve():
    n,k =map(int, input().split())
    a = list(map(int, input().split()))
    
    l = 0
    count = 0
    r = k
    while r<n:
        window = a[l:r+1]
        for i in range(k+1):
            window[i]=window[i]*2**i
        
        # print(window)
        flag = True
        for i in range(1,len(window)):
            if window[i-1]>=window[i]:
                flag = False

        if flag:
            count+=1
        
        l+=1
        r+=1


    return count






t = int(input())
for _ in range(t):
    print(solve())