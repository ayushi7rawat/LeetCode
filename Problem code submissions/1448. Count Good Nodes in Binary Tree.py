#1448. Count Good Nodes in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    total = 0
    def goodNodes(self, root: TreeNode) -> int:
        
        def traverse(root, max = None):
            if root == None:
                return
            
            if max == None:
                max = root.val 
                
                traverse(root.left, max)
                traverse(root.right, max)
                
                self.total += 1
                
            else:
                if(root.val >= max):
                    max = root.val
                    self.total += 1
                    
                traverse(root.left, max)
                traverse(root.right, max)          
            return
        
        traverse(root,None)
        return self.total