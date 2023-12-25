#User function Template for python3
from collections import defaultdict,deque
class Solution:
    def findOrder(self,alien_dict, N, K):
        # code
        ans = ''
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for i in range(N-1):
            s1 = alien_dict[i]
            s2 = alien_dict[i+1]
            for x,y in zip(s1,s2):
                if x!=y:
                    graph[x].append(y)
                    indegree[y]+=1
                    break
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        
        # print(graph)
        # print(indegree)
        
        queue = deque()
        for i in range(k):
            if indegree[alpha[i]]==0:
                queue.append(alpha[i])
        
        # print(queue)
        
        while queue:
            node = queue.popleft()
            
            ans+=node
            
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
                
        
        return ans
            
                    
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends