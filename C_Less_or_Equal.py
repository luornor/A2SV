n,k = map(int,input().split())

a = list(map(int,input().split()))
count = 0
for x in range(1,10^9):
    if x<=a[x]:
        count+=1

if count==0:
    print(-1)
else:
    print(count)
