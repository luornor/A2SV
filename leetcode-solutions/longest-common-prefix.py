class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word: str) -> None:
            curr = self.root
            
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()

                curr = curr.children[c]
            curr.is_end=True
            
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_word = strs[0]
        for i in range(1,len(strs)):
            if len(strs[i]) < len(min_word):
                min_word=strs[i]

        for word in strs:
            self.insert(word)

        curr = self.root
        res = ''

        if len(curr.children)>1:
            return res

        for c in min_word:
            if len(curr.children)>1:
                return res
            res+=c
            curr = curr.children[c]


        return res
        
        
            
            

        

        
        