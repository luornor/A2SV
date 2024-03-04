
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.count = 0
        self.children = {}

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

    def prefixscore(self,word):
        curr = self.root
        score = 0

        for c in word:
            if c in curr.children:
                score += curr.children[c].count
                curr = curr.children[c]
            else:
                break

        return score
        
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = []

        for word in words:
            self.insert(word)

        for word in words:
            curr = self.prefixscore(word)
            res.append(curr)

        return res

        