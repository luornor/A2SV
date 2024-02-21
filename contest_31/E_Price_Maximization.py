def solve():
    n,k = map(int,input().split())
    a = [0]
    l = 1
    r = n
    for x in map(int, input().split()):
        n += x // k
        a.append(x % k)
    
    a.sort()
    while l < r:
        if a[l] + a[r] >= k:
            r -= 1
        l += 1
        
    return n - r

	 			 			  	   	   				  		 	

t = int(input())
for _ in range(t):
    print(solve())


     			  		 			   		 					 	