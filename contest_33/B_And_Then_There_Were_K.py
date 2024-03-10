
def solve():
    n = int(input())
    x = n.bit_length()

    return 2**(x-1)-1
 
t = int(input())
for _ in range(t):
    print(solve())