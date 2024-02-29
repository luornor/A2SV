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

    def longestWord(self, words: List[str]) -> str:
        for word in words:
            self.insert(word)

        longest_word=''

        def dfs(node,path):
            nonlocal longest_word
            if len(longest_word)<len(path):
                longest_word=path

            elif len(longest_word)==len(path) and path<longest_word:
                longest_word=path
            
            for char, child in node.children.items():
                if child.is_end:
                    dfs(child, path+char)


        dfs(self.root,'')
        return longest_word
        




        

        