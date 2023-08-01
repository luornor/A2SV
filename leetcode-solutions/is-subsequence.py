def isSubsequence(s,t):
    l = 0
    r = 0
    n = len(t)
    while r<n:
        if l<len(s) and s[l]==t[r]:
            l+=1
            r+=1
        else:
            r+=1

    return l==len(s)