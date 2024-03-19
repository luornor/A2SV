# def heappop(heap):
#     if not heap:
#         return None
#     min_value = heap[0]
#     heap[0] = heap[-1]
#     heap.pop()
#     current = 0
#     heapify_down(heap,len(heap),current)
#     return min_value

# def swap(heap, i, j):
#     heap[i], heap[j] = heap[j], heap[i]

# def heapify_down(heap, n, current):
#     small_child = current
#     left = 2 * current + 1
#     right = 2 * current + 2
   
#     if left < n and heap[left] < heap[small_child]:
#         small_child = left
       
#     if right < n and heap[right] < heap[small_child]:
#         small_child = right
           
#     if small_child != current:
#         swap(heap,current, small_child)
#         heapify_down(heap,n,small_child)


# def test():
#     heap = [2, 4, 5, 7, 9, 10]
#     min_val = heappop(heap)
#     assert min_val == 2, f"Error: expected 2, but got {min_val}"
#     assert heap == [4, 7, 5, 10, 9], f"Error: expected [4, 7, 5, 10, 9], but got {heap}"

#     heap = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     min_val = heappop(heap)
#     assert min_val == 1, f"Error: expected 1, but got {min_val}"
#     assert heap == [2, 4, 3, 8, 5, 6, 7, 9], f"Error: expected [2, 4, 3, 8, 5, 6, 7, 9], but got {heap}"

#     print("Great Job !!!")
# test()

# class TrieNode:
#     def __init__(self):
#         self.is_end = False
#         self.children = [ None for _ in range(26)]
        # self.children = {}

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         curr = self.root
        
#         for c in word:
#             idx = ord(c)-ord('a')
#             if not curr.children[idx]:
#                 curr.children[idx] = TrieNode()

#             curr = curr.children[idx]
#         curr.is_end=True

#     def searchorStartwith(self,word: str,prefix=False) -> bool:
#         curr = self.root

#         for c in word:
#             idx = ord(c)-ord('a')
#             if not curr.children[idx]:
#                 return False
            
#             curr = curr.children[idx]
            
#         return curr.is_end if not prefix else True

#sieve of eratosthenes
from math import sqrt


def generate_primes(num):
    
    marked = [False]* num

    for i in range(2,int(sqrt(num))+1):
        for j in range(i*i,num,i):
             if j%i==0:
                marked[j]=True
                
                                
    res = []
    for i in range(2,len(marked)):
        if not marked[i]:
              res.append(i)
              
    return res

print(generate_primes(10))