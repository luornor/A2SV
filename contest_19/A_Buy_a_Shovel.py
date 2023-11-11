def solve(k,r):
    #minimun number of shovels
    shovel = 1
    #the shovel price must be divisible either
    #by to r or 10 keep buying shovels
    while (k*shovel)%10 !=0 and (k*shovel)%10 !=r:
        shovel+=1

    print(shovel)




k,r = map(int,input().split())
solve(k,r)