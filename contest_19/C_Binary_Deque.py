def solve(a,n,s):
    #no possible solution
    if s>sum(a):
        print(-1)
    else:
        ans=0
        l=0
        r=0
        curr_sum=0
        while r<n:
            #prefix sum
            curr_sum+=a[r]
            #find maximum subarray with sum equal to s
            #reduce window if subarray sum is greater than s
            while curr_sum>s:
                curr_sum-=a[l]
                l+=1
            if curr_sum==s:
                ans=max(ans,r-l+1)
            r+=1
        print(n-ans)


t  = int(input())
for _ in range(t):
    n,s = map(int,input().split())
    a=list(map(int,input().split()))
    solve(a,n,s)


    

            

            

