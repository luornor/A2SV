from collections import defaultdict
    
def solve():
    n,k = map(int, input().split()) 
    s = input()

    check = ''
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(k):
        check+=alpha[i]

    hmap = defaultdict(int)
    for c in s:
        hmap[c] += 1

    for c in check:
        if c not in hmap:
            return 0

    return min(hmap.values())*k


print(solve())

    
