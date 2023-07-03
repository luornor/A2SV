q = int(input())

def solve(a,b,c):
    # a, b, c = sorted([a, b, c])
    # if c - b > 1:
    #     c -= 1
    # elif b - a > 1:
    #     a += 1
    # return (b - a) + (c - b) + (c - a)
    # Since each friend can move no more than once,
    # subtracting 4 accounts for the fact that the total pairwise distance can be reduced by 2 for each friend.
    return max(0,abs(a-b)+abs(a-c)+abs(b-c)-4)
    
        


for _ in range(q):
    a,b,c = map(int,input().split())
    print(solve(a,b,c))