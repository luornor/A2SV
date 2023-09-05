def solve(n,r,m,b):
    max_f = 0
    r_sum = [0] 
    b_sum = [0]
    count = 0
    for num in r:
        count+=num
        r_sum.append(count)
    count = 0
    for num in b:
        count+=num
        b_sum.append(count)

    for i in range(n+1):
        for j in range(m+1):
            max_f = max(max_f, r_sum[i] + b_sum[j])
    # print(r_sum)
    return max_f

t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    result = solve(n, r, m, b)
    print(result)
    
