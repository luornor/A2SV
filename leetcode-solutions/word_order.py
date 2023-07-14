n = int(input())

word_list = [input() for _ in range(n)]

dict = {}
for item in word_list:
    if item in dict:
        dict[item]+=1
    else:
        dict[item]=1
print(len(dict))
for v in dict.values():
    print(v,end=" ")
    

