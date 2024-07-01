for _ in range(int(input())):
    a,b = map(int, input().split())
    
    score = 1
    
    a_fact = 1
    while a>0:
        a_fact = a_fact * a
        a-=1

    b_fact = 1
    while b>0:
        b_fact = b_fact * b
        b-=1
    
    n =  a_fact//b_fact
    
    prime = 3
    while n>0:
        score+=1
        n = n//prime
        prime+=2

    print(score)