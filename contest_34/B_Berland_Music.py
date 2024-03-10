def solve():
    n = int(input())

    p = list(map(int,input().split()))
    s = input()
    
    #bring zeros first
    songs = sorted([[s[i],p[i],i] for i in range(n)])
    res = [0]*n

    # print(songs)
    for i in range(n):
        # print(res)
        res[songs[i][2]] = i+1


    # print(songs)


    return res
  

    
t = int(input())
for _ in range(t):
    print(*solve())