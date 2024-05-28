n = int(input())
a = list(map(int,input().split()))
#chest biceps and back
#1 4 7
chest = 0
#2 5 8
biceps = 0
back = 0

for i in range(n):
    if i%3==0:
        chest+=a[i]
    elif i%3==1:
        biceps+=a[i]
    else:
        back+=a[i]

if chest > biceps and chest > back:
    print("chest")
elif biceps > chest and biceps > back:
    print("biceps")
else:
    print("back")
    