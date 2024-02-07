def solve():
    n,k =map(int, input().split())
    a = list(map(int, input().split()))
    
    valid = True
    count = 0
    l = 0
    r = k
    while l< n-k:
        if valid:
            count+=1

        valid = True
        for i in range(k):
            if 2 ** (i + 1) * a[l + i] >= 2 ** i * a[l + i + 1]:
                valid = False
                break

        if valid:
            r+=1
        else:
            l+=1

    return count


    
    

t = int(input())
for _ in range(t):
    print(solve())