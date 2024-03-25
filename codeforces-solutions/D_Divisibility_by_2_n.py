def solve():
    n = int(input())
    a = list(map(int,input().split()))

    def count_two(num):
        count = 0
        while num%2==0:
            count+=1
            num//=2
        return count
    
    total_twos = sum(count_two(num) for num in a)
    
    if total_twos>=n:
        return 0
    
    indx = []
    for i in range(1,n+1):
        if count_two(i)>0:
            indx.append(count_two(i))

    # print(indx)
    #for least number of operations
    indx.sort(reverse=True)
    ops = 0
    for count in indx:
        total_twos+=count
        ops+=1
        if total_twos>=n:
            return ops
    
    return -1

t = int(input())
for _ in range(t):
    print(solve())
