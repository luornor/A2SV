def solve():
    s,t = map(str, input().split())
    check = []
    c = ''
    for i in range(len(s) - 1, -1, -1):
        if s[i] in t:
            if t.count(s[i]) > check.count(s[i]):
                check.append(s[i])
                c += s[i]
                
    if t == c[::-1]:
        return 'YES'
    else:
        return 'NO'


for _ in range(int(input())):
    print(solve())