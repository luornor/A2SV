def solve(n,k,a):
    # Sort the sequence
    a.sort()
    #3 7 5 1 10 3 20
    #1 3 3 5 7 10 20 k = 2
    # k = 4
    #1 3 3 5 7 10 20
    if k==0 and a[0]>1:
        print(1)

    elif k == 0 and a[0] == 1:
        print("-1")
    elif k <= n - 1:
        if a[k - 1] != a[k]:
            print(a[k - 1])
        else:
            print("-1")
    elif k == n:
        print(a[k - 1])
    
        


       




n,k = map(int,input().split())

a = list(map(int,input().split()))

solve(n,k,a)



