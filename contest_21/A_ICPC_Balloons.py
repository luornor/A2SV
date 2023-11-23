t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    seen = set()
    ans = 0
    for ch in s:
        if ch in seen:
            ans+=1
        else:
            seen.add(ch)
            ans+=2

    print(ans)
