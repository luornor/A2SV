t = int(input())

for _ in range(t):
    s = input()
    l = 0
    r = 2*len(s)
    n = len(s)
    while l<r:
        mid = (l+r)//2
        
        leftmost = 0
        rightmost = 0

        for i in range(n):
            if s[i] == 'L':
                leftmost = max(leftmost - mid, 0)
            else:
                rightmost = min(rightmost + mid, n + 1)

        if leftmost >= rightmost:
            r = mid
        else:
            l = mid + 1

    print(l)

