class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def insert(self,word):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c]=Trie()
            curr = curr.children[c]
        curr.is_end=True
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)

        res = []
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        def backtrack(node,word,r,c):
            if node.is_end:
                res.append(word)
                node.is_end=False

            if r < 0 or r >= n or c < 0 or c >= m:
                return

            curr = board[r][c]
            if curr not in node.children:
                return
            board[r][c] = '#'
            for x,y in directions:
                backtrack(node.children[curr],word+curr,r+x,c+y)
            
            board[r][c] = curr
        
        for i in range(n):
            for j in range(m):
                backtrack(trie,'',i,j)

        return res