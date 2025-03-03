# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)   # Önce sol alt ağacı gez
            dfs(node.right)  # Sonra sağ alt ağacı gez
            result.append(node.val)  # En son düğümün kendisini ekle
        
        dfs(root)
        return result
