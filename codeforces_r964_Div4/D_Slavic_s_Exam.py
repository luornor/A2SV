def solve():
    s = list(input())
    t = list(input())
    
    j = 0 
    
    for i in range(len(s)):
        if s[i] == '?':
            if j < len(t):
                s[i] = t[j]
                j += 1
            else:
                s[i] = 'a'  
        elif j<len(t) and s[i] == t[j]:
            j += 1
    
    # After loop, check if all characters in t were matched
    if j == len(t):
        return 'YES', ''.join(s)
    else:
        return 'NO',None

for _ in range(int(input())):
    result, modified_s = solve()
    print(result)
    if result == 'YES':
        print(modified_s)
