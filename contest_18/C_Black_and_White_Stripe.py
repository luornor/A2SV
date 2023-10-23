def solve(a, n, k):
    l=0
    hmap={'B':0,'W':0}
    min_w = k
    r=0
    while r<n:
        hmap[a[r]] = hmap.get(a[r],0)+1
        if r-l+1>=k:
            min_w = min(min_w,hmap['W'])
            hmap[a[l]]-=1
            l+=1
        r+=1
    print(min_w)


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    paper = input()
    solve(paper, n, k)


