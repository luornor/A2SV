t = int(input())

def solve():
    len_s,curr_color = input().split()
    len_s = int(len_s)
    colors = input()
    # concatenate the string
    colors += colors
    ans = float('-inf')
    for i in range(len_s): #number of iterations
        if colors[i]==curr_color:
            for j in range(i+1,2*len_s):
                if colors[j]== 'g':
                    ans = max(ans,j-i)
                    break # why?? becos we need to find minimum time

for _ in range(t):
    solve()