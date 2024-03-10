t = int(input())
for _ in range(t):
    a = list(map(int,input().split()))
    count = 0
    check = a[0]
    for i in range(1,len(a)):
        if check<a[i]:
            count+=1

    print(count)