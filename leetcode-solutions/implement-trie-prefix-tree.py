class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26)]
        # self.children = {}
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            idx = ord(c)-ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()

            curr = curr.children[idx]
        curr.is_end=True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            idx = ord(c)-ord('a')
            if not curr.children[idx]:
                return False
            
            curr = curr.children[idx]
            
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        start = self.root
        for c in prefix:
            idx = ord(c)-ord('a')
            if not start.children[idx]:
                return False
            
            start = start.children[idx]
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)