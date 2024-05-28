n = int(input())
a = list(map(int,input().split()))

cards = list(enumerate(a,start=1))
cards.sort(key=lambda x: x[1])
pairs = []

for i in range(n//2):
    first = cards[i][0]
    second  = cards[n-i-1][0]
    pairs.append((first,second))

for pair in pairs:
    print(pair[0],pair[1])