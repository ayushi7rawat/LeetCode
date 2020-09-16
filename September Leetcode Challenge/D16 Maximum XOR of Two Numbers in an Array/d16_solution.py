class Solution:
'''
Problem Name: Maximum XOR of Two Numbers in an Array
Author: Ayushi Rawat
Date: 16-09-2020
'''
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2
        
        nums_bits = [[(x>>i) & 1 for i in reversed(range(L))] for x in nums]
        
        root = {}
        
        for num, bits in zip(nums, nums_bits):
            node = root
            
            for bit in bits:
                node = node.setdefault(bit, {})
                
            node['#'] = num
            
        max_xor = 0
        
        for num, bits in zip(nums, nums_bits):
            node = root
            
            for bit in bits:
                toggled_bit = 1 - bit
                
                if toggled_bit in node:
                    node = node[toggled_bit]
                else:
                    node = node[bit]
                    
            max_xor = max(max_xor, node['#'] ^ num)
        return max_xor
    