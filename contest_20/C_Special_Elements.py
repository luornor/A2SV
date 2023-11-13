def solve(n, a):
    #treat array as prefix array
    count = [0] * (n + 1)

    special_count = 0
    for i in range(n):
        count[a[i]]+=1

    for i in range(n):
        curr_num = a[i]
        for j in range(i + 1, n):
            curr_num+=a[j]
            if curr_num<=n:
                special_count+=count[curr_num]
                count[curr_num]=0
            

    return special_count


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    special_count = solve(n, a)

    print(special_count)