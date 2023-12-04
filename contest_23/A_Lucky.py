def solve():
    s = input()
    ps = []
    curr = 0
    for i in range(len(s)):
        curr+=int(s[i])
        ps.append(curr)
    pre = 0
    suff = []
    for i in range(len(s)-1,-1,-1):
        pre+=int(s[i])
        suff.append(pre)
    suff=suff[::-1]
    if ps[2]==suff[len(s)-3]:
        return 'YES'
    else:
        return 'NO'


t = int(input())
for _ in range(t):
    print(solve())