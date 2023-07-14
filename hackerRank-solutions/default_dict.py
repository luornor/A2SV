from collections import defaultdict
A = defaultdict(list)

a,b = input().split()
for i in range(int(a)):
    word = input()
    A[word].append(str(i+1))


for j in range(int(b)):
    letter = input()
    if letter in A.keys():
        print(' '.join(A[letter]))
    else:
        print(-1)

        

