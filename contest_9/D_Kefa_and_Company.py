def solve(friend,n,d):
    friend.sort()
    max_friendship_factor = 0
    left = 0
    total_factor = 0
    for r in range(n):
        while friend[r][0]-friend[left][0]>=d:
            total_factor -= friend[left][1]
            left+=1
        total_factor += friend[r][1]
        max_friendship_factor = max(max_friendship_factor,total_factor)
    print(max_friendship_factor)

    

n,d = map(int, input().split())
friend = []
for _ in range(n):
    m,s = map(int,input().split())
    friend.append((m,s))

solve(friend,n,d)
