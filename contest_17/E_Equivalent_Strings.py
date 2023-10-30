mem = {}
def equiv_strings(a,b):
    #base case if u can no longer divide the string
    if len(a)%2 !=0:
        return a==b
    #to avoid recomputation
    if (a,b) in mem:
        return mem[(a,b)]
    
    
    #divide string
    a1 = a[:len(a)//2]
    a2 = a[len(a)//2:]
    b1 = b[:len(b)//2]
    b2 = b[len(b)//2:]

    mem[(a,b)]= (equiv_strings(a1,b1) and equiv_strings(a2,b2)) or (equiv_strings(a1,b2) and equiv_strings(a2,b1))
    
    return mem[(a,b)]
    
a = input()
b = input()

if equiv_strings(a,b):
    print('YES')
else:
    print('NO')



