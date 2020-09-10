# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
'''
Problem Name: Sum of Root To Leaf Binary Numbers
Author: Ayushi Rawat
Date: 08-09-2020
'''
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def preorder(r, cur_number):
            nonlocal root_to_leaf
            if r:
                cur_number = (cur_number << 1) | r.val
                # if it's a leaf, update root-to-leaf sum
                if not (r.left or r.right):
                    root_to_leaf += cur_number
                    
                preorder(r.left, cur_number)
                preorder(r.right, cur_number) 
        
        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf
        
     