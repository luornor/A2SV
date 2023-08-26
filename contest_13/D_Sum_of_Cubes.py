from math import pow
def solve(x):
    cube_root = int(pow(x, 1/3)) + 1
    for a in range(1, cube_root):
        b_cube = x - a**3
        if b_cube <= 0:
            break
        b = round(pow(b_cube, 1/3))
        if a**3 + b**3 == x:
            return 'YES'
    return 'NO'



t = int(input())
for _ in range(t):
    x = int(input())
    print(solve(x))