if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    if n<0:n=abs(n)
    ans = [[i,j,k] for i in range(n+x) if i<=x for j in range(n+y) if j<=y for k in range(n+z) if k<=z and i+j+k != n]
    print(ans)


    