def solve():
    n,k = map(int,input().split())
    a = list(map(int, input().split()))
    
    l = 1
    r = n
    for i in range(n):
        n += a[i] // k
        a[i] = a[i]%k
    a = [0] + a
    a.sort()
    while l < r:
        if a[l] + a[r] >= k:
            r -= 1
        l += 1
        
    return n - r
			  	   	   				  		 	

t = int(input())
for _ in range(t):
    print(solve())
	 			   		 					 	