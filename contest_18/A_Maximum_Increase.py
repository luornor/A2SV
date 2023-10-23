n=int(input())
a=list(map(int,input().split()))

l=0
r=0
res = 0
while r<n-1:
    if a[r]<a[r+1]:
        res=max(res,r-l+1)
    else:
        l=r+1
    r+=1

print(res+1)