def solve(a,n):
    #1 2 0
    #prefix_sum = [0,1,3,3]
    #[1,2,4,4]
    # count = 0
    # prefix_sum = [0] * (n+1)
    # prefix_sum[0] = a[0]
    # for i in range(n):
    #     prefix_sum[i + 1] = prefix_sum[i] + a[i]
    # prefix_sum = [0]
    # val = 0
    # for num in a:
    #     val+=num
    #     prefix_sum.append(val)
    # occurrences = {}
    # print(prefix_sum)
    # for i in range(n+1):
    #     diff = prefix_sum[i] - i
    #     count += occurrences.get(diff, 0)
    #     occurrences[diff] = occurrences.get(diff, 0) + 1
    # print(count)

    #1 2 0
    


















        
            

t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    arr = [int(x) for x in a]
    solve(arr,n)