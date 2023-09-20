def solve(n,t,a):
    books=0
    time=0
    count=0
    l=0
    r=0
    while r<n:
        time+=a[r]
        count+=1
        while time>t:
            time-=a[l]
            count-=1
            l+=1
        r+=1
        books=max(books,count)
    print(books)
    

n,t=map(int,input().split())
a = list(map(int,input().split()))
solve(n,t,a)