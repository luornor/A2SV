class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end=True

    def search(self, word: str) -> bool:

        def helper(word,node,idx):
            if idx==len(word):
                return node.is_end

            if word[idx] !='.':
                if  word[idx] not in node.children:
                    return False
                node = node.children[word[idx]]
                if helper(word,node,idx+1):
                    return True


            if word[idx]=='.':
                for c in node.children.values():
                    if helper(word,c,idx+1):
                        return True
            

        return helper(word,self.root,0)

            
                
                  

            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)