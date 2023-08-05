def solve(n,s):
    l = 0
    r = n-1
    is_palidrome = False
    while l<r:
        if s[l]==s[r]:
            s = inversion(s,l,r)
            if s == s[::-1]:
                is_palidrome==True
                break
        r-=1
        l+=1
        
    if is_palidrome:
        print('YES')
    else:
        print('NO')

def inversion(s,l,r):
    s_list = list(s)
    for i in range(l, r + 1):
        if s_list[i] == '0':
            s_list[i] = '1'
        else:
            s_list[i] = '0'
    return ''.join(s_list)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    solve(n,s)