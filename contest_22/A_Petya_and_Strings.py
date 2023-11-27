def solve():
    a= input().lower()
    b = input().lower()
    
    l =0
    r = 0
    ans = 0
    while l<len(a) and r<len(b):
        if a[l]==b[r]:
            ans = 0  
        elif a[l]<b[r]:
            ans = -1
            break
        else:
            ans = 1
            break

        l+=1
        r+=1
    return ans


print(solve())