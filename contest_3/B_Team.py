n = int(input())
def solve(s):
    sure = []
    for item in s:
        if item.count(1)>=2:
            sure.append(1)
    print(len(sure))
    
    
    

problems = []
counter = 0
for _ in range(n):
    s = list(map(int,input().split()))
    problems.append(s)
    total = sum(s)
    if total >=2:
        counter+=1
print(counter)
# solve(problems)