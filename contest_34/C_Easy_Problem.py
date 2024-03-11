from collections import defaultdict
import sys
import threading

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
 

def main():
    n = int(input())
    s = input()
    a = list(map(int,input().split()))

    check = "hard"
    memo = {}
    def dp(i,j):
        if (i,j) in memo:
            return memo[(i,j)]
        
        if j==len(check):
            return float('inf')
        
        if i==len(s):
            return 0
        
        if s[i]==check[j]:
            memo[(i,j)] = min(dp(i+1,j)+a[i],dp(i+1,j+1))

        else:
            memo[(i,j)] = dp(i+1,j)

        return memo[(i,j)]
        
    print(dp(0,0))
   

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()