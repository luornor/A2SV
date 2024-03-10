from collections import defaultdict
import sys
import threading
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
 
def main():
    def solve():
        n = int(input())
        graph = defaultdict(list)

        for _ in range(n-1):
            u,v = map(int,input().split())
            graph[u].append(v)
            graph[v].append(u)

        ch = [0] * 300005
        dp = [0] * 300005

        def dfs(p, q):
            ch[p] = 1
            dp[p] = 0
            s = 0
            for it in graph[p]:
                if it != q:
                    dfs(it, p)
                    s += dp[it]
                    ch[p] += ch[it]
            
            for it in graph[p]:
                if it != q:
                    dp[p] = max(dp[p], s - dp[it] + ch[it] - 1)

        dfs(1, 0)
        return dp[1]

    t =int(input())
    for _ in range(t):
        print(solve())
    

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()