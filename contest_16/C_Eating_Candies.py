def solve(n,candies):
    l=0
    r=n-1
    alice_count=0
    bob_count=0
    alice_w=0
    bob_w=0
    ans=0
    while l<=r:
        if alice_w<bob_w:
            alice_count+=1
            alice_w+=candies[l]
            l+=1
        else:
            bob_w+=candies[r]
            bob_count+=1
            r-=1
        if alice_w==bob_w:
            ans=(bob_count+alice_count)
    print(ans)

    
        
    


    
    
t = int(input())
for _ in range(t):
    n=int(input())
    candies = list(map(int,input().split()))
    solve(n,candies)