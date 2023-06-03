# Enter your code here. Read input from STDIN. Print output to STDOUT
n_english = int(input())

s = set(input().split())

n_french = int(input())

f =set(input().split())
if n_english+ n_french<1000:
    print(len(s.difference(f)))