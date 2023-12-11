def solve():
    n = input()
    flag = False
    for i in n:
        if (int(i) % 2 == 0):
            flag = True
            break
    if not flag:
        return -1   
     
    if int(n) % 2 == 0:
        return 0
    if int(n[0]) % 2 == 0:
        return 1
        
    return 2

    


t = int(input())
for _ in range(t):
    print(solve())