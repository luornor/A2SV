def solve():
    s = input()
    ans=''
    if len(s)==2:
        return s
    for i in range(0,len(s),2):
        ans+=s[i]
    ans+=s[-1]
    return ans


t = int(input())
for _ in range(t):
    print(solve())