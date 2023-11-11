def solve(num):
    ans = 0
    #check  by how much i need to reduce a number 
    #so it can be possible to represent it as a power of ten
    while 10**ans<=num:
        ans+=1
    # print(ans)
    return num-10**(ans-1)

t= int(input())

for _ in range(t):
    price = int(input())
    print(solve(price))
    # print(res)