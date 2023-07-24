t = int(input())

def solve(len_s,curr_color,colors):
    len_s = int(len_s)
    colors += colors
    ans = 0
    if len_s==1 and colors[0]=='g':
        print(0)
        return
    
    for i in range(len_s): #number of iterations
        if colors[i]==curr_color:
            for j in range(i+1,2*len_s):
                if colors[j]== 'g':
                    ans = max(ans,j-i)
                    break # why?? becos we need to find minimum time

    print(ans)

for _ in range(t):
    len_s,curr_color = input().split()
    colors = input()
    solve(len_s,curr_color,colors)