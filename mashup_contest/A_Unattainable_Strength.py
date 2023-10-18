def solve(n,x):

    x.sort()

    smallest_energy = 1

    for i in range(n):
        if x[i] <= smallest_energy:
            smallest_energy += x[i]
        else:
            break

    print(smallest_energy)




n=int(input())
x=list(map(int,input().split()))

solve(n,x)


