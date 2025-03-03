# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        if root is None:
            return None  # Boş düğümse geri dön
        
        # Sol ve sağ alt ağaçları takas et
        root.left, root.right = root.right, root.left  
        
        # Aynı işlemi alt ağaçlara uygula
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        
