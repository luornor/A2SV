class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
        self.count = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word: str) -> None:
            curr = self.root
            
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()

                curr.children[c].count+=1
                curr = curr.children[c]

            curr.is_end=True
            

            
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ''
        
        for word in strs:
            self.insert(word)
    
        longest_word = max(strs,key=len)
        curr = self.root
        for c in longest_word:
            if c in curr.children:
                if curr.children[c].count==len(strs):
                    res+=c
                if curr.children[c].count<len(strs):
                    break
                curr = curr.children[c]

        return res
        