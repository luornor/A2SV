n = int(input())
s = input()
a = list(map(int,input().split()))

check = 'hard'
is_hard = False
i = 0
idx = []
for c in s:
    if i==len(check):
        is_hard=True
        break
    if c==check[i]:
        idx.append(a[i])
        i+=1

if is_hard:
    print(idx)
else:
    print(0)

