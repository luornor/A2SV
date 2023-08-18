
t = int(input())
#oelhl
#o-1
#e-1
#l-2
#h-1
def solve(s):
    hashset = set()
    ans = []

    for c in s:
        if c not in hashset:
            hashset.add(c)
        else:
            ans.append(c)
            hashset.remove(c)

    ans += ans
    for char in hashset:
        ans.append(char)
    
    print(''.join(ans))


for _ in range(t):
    s = input()
    solve(s)