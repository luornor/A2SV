from collections import Counter


def solve():
    n = int(input())
    s = input()
    char_count = Counter(s)
    max_count = max(char_count.values())

    if 2*max_count>n:
        return (2*max_count)- len(s)
    
    elif 2*max_count<n:
        if len(s)%2==0:
            return 0
        else:
            return 1
    else:
        return 0
    


"""
avbvvcvvvd
a -1
b-1
c-1
d-1
v-6
"""

t = int(input())
for _ in range(t):
    print(solve())
