n = int(input())
a = list(map(int, input().split()))

l = 0
r=1
while l<n:
    if (a[l] + a[r])%2 !=0:
        a[l],a[r]=a[r],a[l]
        break
    else:
        r+=1
    l+=1
   
print(*a)