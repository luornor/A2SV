def solve():
    n,k,x = map(int,input().split())
    available_numbers = [i for i in range(1, k + 1) if i != x]

    m = []
    for num in sorted(available_numbers, reverse=True):
        while n >= num:
            n -= num
            m.append(num)

    if n==0:
        return "YES",len(m),m
    else:
        return "NO",len(m),m
    


for _ in range(int(input())):
    can,len_m,m = solve()
    if can=="NO":
        print(can)
    else:
        print(can)
        print(len_m)
        print(*m)