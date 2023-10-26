n,m,s,A,B= map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort()
l=0
r=0
weight=0
cost=1
while r<n:
    weight+=A
    cost+=a[r]
    r+=1
    while weight>s:
        weight-=A
        cost-=a[l]
        l+=1
i=0
j=0
while j<m:
    weight+=B
    cost+=b[j]
    j+=1
    while weight>s:
        cost-=b[i]
        cost-=a[i]
        weight-=B
        weight-=A
        i+=1

print(cost)

