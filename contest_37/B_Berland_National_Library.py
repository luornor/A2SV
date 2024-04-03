
visit = set()
res = 0
for _ in range(int(input())):
    sign, id = input().strip().split()
    if sign == '+':
        visit.add(id)
        res = max(res, len(visit))
    else:
        if id in visit:
            visit.remove(id)
        else:
            res += 1
 
print(res)