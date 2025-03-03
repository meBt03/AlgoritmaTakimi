# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def order(node, total):
            if not node:
                return total
            #Sağ alta geç
            total = order(node.right, total)
            #Düğümün yeni değerini ata
            node.val += total
            #Yeni toplamı ata
            total = node.val
            #Sol altı gez
            return order(node.left, total)
        
        order(root, 0)
        return root
