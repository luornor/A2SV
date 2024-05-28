import itertools

class Node():
    def __init__(self):
        self.blocked = False
        self.child = dict()
        self.parent = None

class Trie():
    def __init__(self):
        self.root = Node()

    def add_word(self, size, id):
        tmp = self.root
        i = 0
        word = [0] * size

        while i < size:
            next_char = -1
            for j in range(2):
                if j not in tmp.child or not tmp.child[j].blocked:
                    next_char = j
                    break

            if next_char == -1:
                if tmp == self.root:  # can't percolate up
                    return False
                else:
                    tmp.blocked = True
                    tmp = tmp.parent
                    i -= 1  # move back up the trie
            else:
                if next_char not in tmp.child:
                    tmp.child[next_char] = Node()
                    tmp.child[next_char].parent = tmp
                tmp = tmp.child[next_char]
                word[i] = chr(next_char + 48)
                i += 1

        tmp.blocked = True
        ans[id] = ''.join(word)
        return True

# Input reading
n = int(input())
lengths = list(map(int, input().split()))
lengths_with_index = sorted((length, index) for index, length in enumerate(lengths))

# Initialize answer array
ans = [''] * n
tree = Trie()
no = False

# Process each length and try to add a word to the trie
for length, index in lengths_with_index:
    if not tree.add_word(length, index):
        no = True
        break

# Output results
if no:
    print("NO")
else:
    print("YES")
    for word in ans:
        print(word)
