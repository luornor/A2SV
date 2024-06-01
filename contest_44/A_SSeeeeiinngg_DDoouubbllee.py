from collections import Counter


def solve():
    s=input()
    double = ''
    for c in s:
        double += c*2

    hmap = Counter(double)
    pali = ''
    for k,v in hmap.items():
        pali += k*(v//2)

    return pali+''.join(reversed(pali))

for _ in range(int(input())):
    print(solve())