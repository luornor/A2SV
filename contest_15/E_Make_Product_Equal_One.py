n = int(input())
a = list(map(int,input().split()))

positive_num = []
negative_num = []
zeros = []
cost = 0

for num in a:
    if num > 0:
        positive_num.append(num)
    elif num < 0:
        negative_num.append(num)
    else:
        zeros.append(num)

for num in positive_num:
    cost+=(num-1)

for num in negative_num:
    cost+=-(num+1)

if len(zeros)>0:
    cost+=len(zeros)
elif len(negative_num)%2==1:
    cost+=2


print(cost)
