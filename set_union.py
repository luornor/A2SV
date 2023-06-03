# Enter your code here. Read input from STDIN. Print output to STDOUT
n_english = int(input())

e = set(input().split())

n_french = int(input())
f = set(input().split())

# if 0<n_english+n_french<1000:
print(len(e.union(f)))

