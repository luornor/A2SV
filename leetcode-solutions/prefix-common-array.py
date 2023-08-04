def findThePrefixCommonArray(A,B):
    n = len(A)
    res = [0]*n
    a_count = [0]*(n+1)
    b_count = [0]*(n+1)
    for i in range(n):
        a_count[A[i]]=1
        b_count[B[i]]=1
        for a,b in zip(a_count,b_count):
            if a==b==1:
                res[i]+=a

    
    return res

A = [1,3,2,4]
B = [3,1,2,4]
print(findThePrefixCommonArray(A,B))
