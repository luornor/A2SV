t = int(input())
def solve(a,n):

    for i in range(1,n):
        if a[i]>= a[i-1]:
            return False
    return True
    

for _ in range(t):
    n = int(input()) #number of cubes
    a = list(map(int,input().split()))
    if solve(a,n):
        print('NO')
    else:
        print('YES')

