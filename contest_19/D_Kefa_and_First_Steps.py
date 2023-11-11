n = int(input())
a = list(map(int,input().split()))

l =0
r = 0
max_len = 0
while r<n:
    if r> 0 and a[r-1]>a[r]:
        l=r
    max_len = max(max_len,r-l+1)
    r+=1

print(max_len)
    