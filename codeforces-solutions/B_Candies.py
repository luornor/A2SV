"""
First, we notice that after each operation, the number of candies is always a odd number.
 So even numbers can not be achieved.
Then consider how the binary representation 
changes for a odd number x, after turn it into 2x+1 or 2x-1

For the 2x+1 operation: …1¯¯¯¯¯¯¯¯¯turns into …11¯¯¯¯¯¯¯¯¯¯¯¯

For the 2x-1 operation: …1¯¯¯¯¯¯¯¯¯turns into …01¯¯¯¯¯¯¯¯¯¯¯¯


So, the operation is just insert a 0/1
before the last digit. And the answer for an odd n
is just the binary representation of n, after removing the last digit.

"""
def solve(n):
    if n % 2 == 0:
        print("-1")
        return
    v = []
    f = 0
    for i in range(29, 0, -1):
        if (n >> i) & 1:
            f = 1
            v.append(2)
        elif f:
            v.append(1)
    print(len(v))
    print(*v)


t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)