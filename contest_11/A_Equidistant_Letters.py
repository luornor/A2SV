
t = int(input())
#oelhl
#o-1
#e-1
#l-2
#h-1
def solve(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    result = ''
    for char, count in sorted_chars:
        result += char * count
    
    if len(result) > 2:
        mid = len(result) // 2
        first_half = result[:mid]
        second_half = result[mid:]
        result = ''
        for i in range(len(first_half)):
            result += first_half[i] + second_half[i]
    
    print(result)


for _ in range(t):
    s = input()
    solve(s)