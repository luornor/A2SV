"""
You are given a rooted tree consisting of n vertices numbered from 1 to n. 
The root is vertex 1 .There is also a string s denoting the color of each vertex: if si=B
, then vertex i is black, and if si=W,then vertex i is white.

A subtree of the tree is called balanced if the number of white vertices 
equals the number of black vertices. Count the number of balanced subtrees.

A tree is a connected undirected graph without cycles. 
A rooted tree is a tree with a selected vertex, which is called the root. 
In this problem, all trees have root 1.

The tree is specified by an array of parents a2,…,an
containing n-1 numbers: ai is the parent of the vertex with the number i for all i=2,…,n.
The parent of a vertex u is a vertex that is the next vertex on a simple path from u
to the root.

The subtree of a vertex u is the set of all vertices that pass through u
on a simple path to the root. For example, in the picture below, 7 is in the subtree of 3
because the simple path 7→5→3→1 passes through 3. 
Note that a vertex is included in its subtree, 
and the subtree of the root is the entire tree.

The picture shows the tree for n=7,a=[1,1,2,3,3,5],and s=WBBWWBW.
The subtree at the vertex 3 is balanced.
Input
The first line of input contains an integer t
(1≤t≤104) — the number of test cases.

The first line of each test case contains an integer n
(2≤n≤4000) — the number of vertices in the tree.

The second line of each test case contains n-1
integers a2,…,an(1≤ai<i) — the parents of the vertices 2,…,n.

The third line of each test case contains a string s
of length n consisting of the characters B and W— the coloring of the tree.

It is guaranteed that the sum of the values n over all test cases does not exceed 2⋅105.

Output
For each test case, output a single integer — the number of balanced subtrees.

Example
input
3
7
1 1 2 3 3 5
WBBWWBW
2
1
BW
8
1 2 3 4 5 6 7
BWBWBWBW
output
2
1
4
Note
The first test case is pictured in the statement. Only the subtrees at vertices 2
and 3 are balanced.

In the second test case, only the subtree at vertex 1 is balanced.

In the third test case, only the subtrees at vertices 1, 3, 5, and 7 are balanced.
"""

import sys
import threading

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        s=input()
        graph = {i+1:[] for i in range(n)}
        for i in range(n-1):
            graph[arr[i]].append(i+2)
        visited = set()
        res = 0
        def dfs(node):
            nonlocal res
            count=1 if s[node-1]=='B' else -1
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    temp=dfs(neighbour)
                    count+=temp
            if count==0:
                res+=1

            return count
        
        for i in range(1,n+1):
            if i not in visited:
                dfs(i)

        print(res)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()