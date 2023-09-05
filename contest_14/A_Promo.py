

n,q = map(int,input().split())
arr = list(map(int,input().split()))
ps = []
arr = sorted(arr,reverse=True)
arr = [0]+arr

count = 0
for num in arr:
    count+=num
    ps.append(count)
for i in range(q):
    x,y = map(int,input().split())
    print(ps[x]-ps[x-y])