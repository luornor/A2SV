from itertools import accumulate


t=int(input())
for i in range(t):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))

    ps=[0]+list(accumulate(a))
        
    # print(ps)
    for _ in range(q):
        currsum=0
        l,r,k=map(int,input().split())
        #sum of subarray
        added_sum = (r-l+1)*k
        currsum+=ps[l-1]+added_sum + ps[n]-ps[r]
        # print(currsum)
        if currsum%2==0:
            print("NO")
        else:
            print("YES")
