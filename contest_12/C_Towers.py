def solve(n,l):
    height = []
    curr_group = {}
    for item in l:
        if item not in curr_group:
            curr_group[item] = [item]
        else:
            curr_group[item].append(item)
    height = list(curr_group.values())
        
    # print(height)
    max_height = 0
    for item in height:
        max_height = max(max_height,len(item))

    res = [max_height,len(height)]
    print(*res)


n = int(input())
l = list(map(int,input().split()))
solve(n,l)
