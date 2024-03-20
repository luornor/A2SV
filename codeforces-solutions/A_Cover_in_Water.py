def solve():
    n = int(input())
    string = input()
    
    return 2 if '...' in string else string.count('.')
        
t = int(input())
for _ in range(t):
    print(solve())