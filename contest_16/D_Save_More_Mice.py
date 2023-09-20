def solve(n,k,cordinates):
    cat=0
    max_mice=0
    cordinates=sorted(cordinates,reverse=True)
    for i in range(k):
        if cat<cordinates[i]:
            remaining_steps=n-cordinates[i]
            max_mice+=1
            cat+=remaining_steps
        else:
            break
    print(max_mice)

t= int(input())
for _ in range(t):
    n,k=map(int,input().split())
    cordinates = list(map(int,input().split()))
    solve(n,k,cordinates)
    