t = int(input())

for _ in range(t):
    s = int(input())
    number = ""
    
    for d in range(9, 0, -1):
        if d <= s:
            number += str(d)
            s -= d
        if s == 0:
            break
    
    print(number[::-1])



        


