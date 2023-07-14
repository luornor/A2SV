# Enter your code here. Read input from STDIN. Print output to STDOUT
n_english = int(input())

s = set(input().split())

n_french = int(input())

f =set(input().split())

print(len(s.difference(f)))