def solve(questions):
    
    #6 4 2 7 2 7--v
    #2 2 4 6 7 7--u
    #2 3 6 
    ans  = 0
    #unsorted preifx
    if questions[0]==1:
        if questions[-2]==0:
            ans = prefix_v[questions[-1]]
        else:
            #prefix[r]-prefix[l-1]
            ans = prefix_v[questions[-1]]-prefix_v[questions[-2]-1]
    else:
        if questions[-2]==0:
            ans = prefix_u[questions[-1]]
        else:
            ans = prefix_u[questions[-1]]-prefix_u[questions[-2]-1]
        
    print(ans)



n = int(input())
v = list(map(int,input().split()))
m = int(input())
prefix_v = [0] * (n + 1)
prefix_v[1] = v[0]
for i in range(1, n):
    prefix_v[i + 1] = prefix_v[i] + v[i]

#sorted prefix
u = sorted(v)
prefix_u = [0] * (n + 1)
prefix_u[1] = u[0]
for i in range(1, n):
    prefix_u[i + 1] = prefix_u[i] + u[i]

for _ in range(m):
    questions = list(map(int,input().split()))
    solve(questions)    