from itertools import accumulate
n,m = map(int,input().split())
a = list(map(int,input().split()))

damage = []
for i in range(n-1):
    if a[i] > a[i+1]:
        damage.append(a[i]-a[i+1])
    else:
        damage.append(0)

ps =[0]+ list(accumulate(damage))

rev = []
for i in range(n-1,0,-1):
    if a[i] > a[i-1]:
        rev.append(a[i]-a[i-1])
    else:
        rev.append(0)

suf = [0]+list(accumulate(rev[::-1]))

for _ in range(m):
    s,t = map(int,input().split())

    if t>s:
        print(ps[t-1]-ps[s-1])

    else:
        print(suf[s-1]-suf[t-1])

    
    

