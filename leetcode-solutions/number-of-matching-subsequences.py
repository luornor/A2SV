class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
    
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.is_end = True

    def is_subsequence(self,word,s):
        i = 0
        for c in s:
            if i==len(word):
                return True
            if c==word[i]:
                i+=1
        
        return i==len(word)

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        for word in words:
            self.insert(word)

        
        memo = {}
        ans = 0
        for word in words:
            count = 0
            if word not in memo:
                if self.is_subsequence(word,s):
                    count+=1
                memo[word]=count
            else:
                count += memo[word]
                
            ans+=count 

        return ans
        