t = int(input())

def solve():
    s = input()
    
    n = len(s)
    ans = [0]
    for i in range(n):
        if s[i]=='R':
            ans.append(i+1)

    ans.append(n+1)
    d = -1
    for i in range(1,len(ans)):
        d = max(d,ans[i]-ans[i-1])

    return d
    # a = list(map(len,input().split('R')))
    # print(a)
    # return max(a)+1


for _ in range(t):
    print(solve())
   

