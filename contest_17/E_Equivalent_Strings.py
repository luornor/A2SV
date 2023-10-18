def equiv_sort(s):
    if len(s) % 2 != 0:
        return s
    
    s1 = equiv_sort(s[:len(s)//2])
    s2 = equiv_sort(s[len(s)//2:])
    
    if s1 < s2:
        return s1 + s2
    else:
        return s2 + s1

a = input()
b = input()

if equiv_sort(a) == equiv_sort(b):
    print("YES")
else:
    print("NO")


