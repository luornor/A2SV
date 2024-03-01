class TrieNode:
    def __init__(self):
        self.num = 0
        self.children = {}


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def int_to_string(self,num,bit_len):
        binary = bin(num)[2:]
        if len(binary)==bit_len:
            return binary
        else:
            x = bit_len-len(binary)
            binary = '0'*x+binary
            return binary


    def insert(self,binary_num):
        curr = self.root
        for bit in binary_num:
            if bit not in curr.children:
                curr.children[bit]=TrieNode()
            curr = curr.children[bit]

        curr.num = int(binary_num,2)


    def nearest(self,num):
        curr = self.root
        
        for bit in num:
            if bit=='1':
                if '0' in curr.children:
                    curr = curr.children['0']
                else:
                    curr = curr.children['1']
            else:
                if '1' in curr.children:
                    curr = curr.children['1']
                else:
                    curr = curr.children['0']

        return curr.num

        
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_num = max(nums)
        n = max_num.bit_length()
        for num in nums:
            bin_num = self.int_to_string(num,n)
            self.insert(bin_num)
    
        max_xor = 0
        for i in range(len(nums)-1):
            bin_num = self.int_to_string(nums[i],n)
            max_xor = max(max_xor, nums[i] ^ self.nearest(bin_num))
        
        return max_xor
