def solve():
    n,k = map(int, input().split())
    s = input()
    ans = 0
    for i in range((k+1)//2):
        hmap = [0]*26
        for j in range(i, n, k):
            hmap[ord(s[j])-97] += 1
            if i!=k-i-1:
                hmap[ord(s[j+k-2*i-1])-97]+=1
        max_freq = max(hmap)
        total_positions = (n // k) * (2 if i != k - i - 1 else 1)
        ans += total_positions - max_freq


    return ans

for _ in range(int(input())):
    print(solve())

