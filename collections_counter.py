# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x  = int(input()) #number of shoes

# ALL Shoes sizes
shoe_sizes = input().split()

N = int(input()) #Number of customers
dict = Counter(shoe_sizes)
total_price = 0
# shoe size and price 
for i in range(N):
    size,price = input().split()
    if size in dict.keys():
        if dict[str(size)]==0:
            continue
        else:
            total_price+=int(price)
            dict[str(size)]-=1
print(total_price)




