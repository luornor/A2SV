from collections import defaultdict
A = defaultdict(list)
B = defaultdict(list)

a,b = input().split()
for _ in range(int(a)):
    A['Group A'].append(input())

for _ in range(int(b)):
    A['Group B'].append(input())

def return_index(list1,n):
    ans = defaultdict(list) 
    for i in range(len(list1)):
        if list1[i]==n:
            ans['indexes'].append(i+1)
    return ans
            

             




if len(A['Group A'])>len(A['Group B']):
    for item in A['Group B']:
       if item in A['Group A']:
            word_index = return_index(A['Group A'],item)
       else:
           print(-1)
    print()
    
else:
    for item in A['Group A']:
        if item in A['Group B']:
            return_index(A['Group B'],item)
        else:
            print(-1)

        

