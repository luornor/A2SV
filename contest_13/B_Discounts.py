
n = int(input()) #num of chocolate bars
a = list(map(int,input().split())) # 
m = int(input()) # num of coupons
q = list(map(int,input().split())) #coupons

a = sorted(a,reverse=True)
total = sum(a)
for num in q:
    print(total - a[num-1])

