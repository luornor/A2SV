if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    ans = [[i,j,k] for i in range(n+1) if i<=x for j in range(n+1) if j<=y for k in range(n+1) if k<=z and i+j+k!=n]
    print(ans)


    