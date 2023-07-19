t = int(input())

def solve(s):
    n = len(s)
    # l = r = 0
    # min_len = float('inf')
    # char_set = {1:0,2:0,3:0}
    # while r<n:
    #     char_set[int(s[r])]+=1
    #     #'1' in char_set and '2' in char_set and '3' in char_set
    #     #check if 1 and 2 and 3 appears more than once
    #     while all(char_set.values()):
    #         min_len = min(min_len,r-l+1)
    #         #reduce window size
    #         char_set[int(s[l])]-=1
    #         l+=1
    #     r+=1

    # if min_len==float('inf'):
    #     print(0)
    # else:
    #     print(min_len)
    #optimised solution
    one = -1
    two = -1
    three = -1
    ans = len(s)+1
    for r in range(n):
        if s[r]=='1':
            one = r
        elif s[r]=='2':
            two = r
        elif s[r]=='3':
            three = r

        if one!=-1 and  two!=-1 and  three!=-1:
            l = min(one,two,three)
            ans = min(ans,r-l+1)
    if ans>n:
        print(0)
    else:
        print(ans)




for _ in range(t):
    s = input()
    solve(s)