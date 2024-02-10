def solve():
    t = int(input())
    for _ in range(t):
        s = list(input())
        c= input()
        
        possible = False

        for i in range(0, len(s), 2):
            if s[i] == c:
                possible = True
                break

        if possible:
            print("YES")
        else:
            print("NO")

        
        
solve()

