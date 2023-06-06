A = set(input())

N = int(input())
sets = [set(input().split()) for i in range(N)]

flag=[]
for item in sets:
    if A.issuperset(item):
        flag.append(True)
    else:
        flag.append(False)
if flag.count(True)==N:
    print(True)
else:
    print(False)

