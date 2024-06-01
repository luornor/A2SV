MOD = 10**9+7
s = input()
n = len(s)

ans = 1
count = 1
for c in s:
    if c=='a':
        count+=1
    elif c=='b':
        ans = (ans*count)%MOD
        count=1

ans = (ans*count)%MOD

print(ans-1)