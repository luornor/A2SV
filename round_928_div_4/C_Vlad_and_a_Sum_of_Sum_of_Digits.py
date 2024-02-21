from collections import defaultdict
from itertools import accumulate


    
arr = []
for i in range(1,200001):
    n = str(i)
    sm = 0
    for i in n:
        sm += int(i)
    arr.append(sm)
    
# print(arr)

arr = list(accumulate(arr))
t = int(input())

for _ in range(t):
    n = int(input())

    print(arr[n-1])
    
    

