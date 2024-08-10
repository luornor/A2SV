def solve(a1, a2, b1, b2):
    configurations = [
        (a1, b1, a2, b2),
        (a1, b2, a2, b1),
        (a2, b1, a1, b2),
        (a2, b2, a1, b1)
    ]
    
    suneet_wins = 0
    
    for a1, b1, a2, b2 in configurations:
        suneet_rounds = 0
        slavic_rounds = 0
        
        if a1 > b1:
            suneet_rounds += 1
        elif a1 < b1:
            slavic_rounds += 1
        
        if a2 > b2:
            suneet_rounds += 1
        elif a2 < b2:
            slavic_rounds += 1
        
        if suneet_rounds > slavic_rounds:
            suneet_wins += 1
    
    return suneet_wins

for _ in range(int(input())):
    a1, a2, b1, b2 = map(int, input().split())
    print(solve(a1, a2, b1, b2))
