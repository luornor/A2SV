t = int(input())

def solve(s):
    n = len(s)
    working = set()
    malfunction = set()

    l = 0
    while l<n:
        if l<n-1 and s[l]==s[l+1]:
            malfunction.add(s[l])
            l+=2
        else:
            working.add(s[l])
            l+=1
    print(''.join(sorted(list(working))))

    

for _ in range(t):
    s = input()
    solve(s)