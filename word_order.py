n = int(input())

word_list = [input() for _ in range(n)]

dict = {}
for item in (word_list):
    a = word_list.count(item)
    dict[item]= a
print(len(dict))
for v in dict.values():
    print(v,end=" ")
    

