k,n,w = map(int,input().split())

money = 0
for i in range(w):
    money+=(i+1)*k
if money<=n:
    print(0)
else:
    print(money-n)
