class Solution:
'''
Problem Name: All Elements in Two Binary Search Trees
Author: Ayushi Rawat
Date: 05-09-2020
'''
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def traverse(node):
            if not node:
                return []
            return [node.val] + traverse(node.left) + traverse(node.right)
 
        res = traverse(root1)
        res += traverse(root2)
        return sorted(res)