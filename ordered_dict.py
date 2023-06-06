from collections import OrderedDict,Counter

item_order = OrderedDict()
    
    
res = []
item_num= int(input())
for _ in range(item_num):
    item_price  = input().split()
    res.append(item_price)

for *item,price in res:
        item = " ".join(item)
        if item in item_order:
            item_order[item]+=int(price)
        else:
            item_order[item]=int(price)
for k,v in item_order.items():
     print(k,v)
    


