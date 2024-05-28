import sys
input = sys.stdin.readline

n = int(input())
S = [input().rstrip() for _ in range(n)]

# Initialize the necessary variables
total_length = 0
start_count = [0] * 26
end_count = [0] * 26

# Precompute lengths and start/end character counts
lengths = []

for s in S:
    length = len(s)
    lengths.append(length)
    total_length += length
    start_count[ord(s[0]) - ord('a')] += 1
    end_count[ord(s[-1]) - ord('a')] += 1

# Initial sum of all lengths paired with all other lengths
sum_all_lengths = total_length * n * 2

# Subtract overlaps
overlap_sum = 0

for s in S:
    first_char_index = ord(s[0]) - ord('a')
    last_char_index = ord(s[-1]) - ord('a')
    # For each string s, subtract the overlap contributions
    overlap_sum += len(s) * (start_count[last_char_index] + end_count[first_char_index])

# Total collapse length calculation
total_collapse_length = sum_all_lengths - overlap_sum

print(total_collapse_length)
