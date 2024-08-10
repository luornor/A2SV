def solve():
    n,s,m = map(int,input().split())
    tasks = []
    for _ in range(n):
        l,r = map(int,input().split())
        tasks.append((l,r))

    #before first task
    l= tasks[0][0]
    if l>=s:
        return 'YES'
    #after last task
    r2 = tasks[-1][1]
    if m-r2>=s:
        return 'YES'
    
    #between tasks
    for i in range(len(tasks)-1):
        r = tasks[i][1]
        l = tasks[i+1][0]
        if (l-r)>=s:
            return 'YES'
        
    return 'NO'
        

for _ in range(int(input())):
    print(solve())