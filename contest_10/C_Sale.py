

n ,m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

r = 0
maxsum=0

while r<m:
    if a[r]<0:
        maxsum+=abs(a[r])
    else:
        break
    r+=1

print(maxsum)


