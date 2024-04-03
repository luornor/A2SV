r1,c1,r2,c2 = map(int, input().split())

#min for rook
rook = 0
if r1==r2 or c1==c2:
    rook=1
else:
    rook=2

bishop =0
row = abs(r1-r2)
col = abs(c1-c2)

if row==col:
    bishop=1
elif abs(row-col) % 2==0:
    bishop=2
else:
    bishop=0

#min for king
king = max(abs(r1-r2),abs(c1-c2))
print(rook,bishop,king)
