# n,k = map(int,input().split())

# group = []
# for _ in range(n):
#     group.append(input())
    

# #if odd
# if k%2!=0:
#     print('First')
# else:
#     print('Second')

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

def insert(trie, word):
    node = trie
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end = True

def can_win(node):
    if not node.children:
        return False
    return not all(can_win(child) for child in node.children.values())

def can_lose(node):
    if not node.children:
        return True
    return any(not can_lose(child) for child in node.children.values())

n, k = map(int, input().split())
strings = [input().strip() for _ in range(n)]

trie = TrieNode()
for s in strings:
    insert(trie, s)

first_player_can_win = can_win(trie)
first_player_can_lose = can_lose(trie)

if first_player_can_win and (first_player_can_lose or k % 2 == 1):
    print("First")
else:
    print("Second")
