def solve():
    rook = input()
    col = rook[0]
    row = rook[1]
    res = []
    letters = ['a','b','c','d','e','f','g','h']
    for i in range(1,9):
        if f"{col}{i}"!= rook:
            res.append(f"{col}{i}")

    for j in range(8):
        if f"{letters[j]}{row}"!= rook:
            res.append(f"{letters[j]}{row}")
    
    for item in res:
        print(item)


t = int(input())

for _ in range(t):
    solve()