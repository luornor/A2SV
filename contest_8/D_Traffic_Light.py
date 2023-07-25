def solve(n,current_color,colors):
    #find index of last green in last half of string
    n = int(n)
    #for cyclic check
    colors+=colors
    last_green = 0
    ans = 0
    for i in range(2*n-1, n-1,-1):
        if colors[i]=='g':
            last_green = i

    #find the index of current color and in first half of strin
    for i in range(n,-1,-1):
        #check for green in first half
        if colors[i]=='g':
            last_green=i
        if current_color==colors[i]:
            ans = max(ans, last_green-i)
    print(ans)




t = int(input())
for _ in range(t):
    n, current_color = input().split()
    colors = input()
    solve(n,current_color,colors)