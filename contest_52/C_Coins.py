def solve():
    n = int(input())
    min_coins = float('inf')  
    
    for i in range(n // 5 + 1):  
        rem = n - i * 5          
        if rem % 3 == 0:        
            return 0 
        else:
            min_coins = min(min_coins, rem % 3)
    
    return min_coins


for _ in range(int(input())):
    print(solve())
