def solve():
    n,m = map(int,input().split())
    k = list(map(int,input().split()))
    c = list(map(int,input().split()))
    
    k.sort(reverse=True)

    min_cost = 0
    for j,num in enumerate(k):
        #to give money or present
        idx = min(j,num-1)
        min_cost += c[idx]
       
    return min_cost
    
t = int(input())
for _ in range(t):
    print(solve())

     			  	 		 	 		      		 			