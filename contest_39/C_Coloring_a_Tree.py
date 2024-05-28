n = int(input())


p = list(map(int,input().split()))
c = list(map(int,input().split()))

p = [0,0] + p
c = [0]+c

# print(p)
# print(c)

steps = 1
for i in range(2,n+1):
    #color child not equal to parent
    if c[i] != c[p[i]]:
        steps+=1

print(steps)