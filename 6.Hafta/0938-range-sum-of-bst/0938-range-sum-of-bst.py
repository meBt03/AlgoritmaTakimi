# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:        
        if not root:
            return 0
        
        total = 0
        
        # Eğer mevcut düğüm aralıktaysa 
        if low <= root.val <= high:
            total += root.val
        
        # Sol daha küçükse sola gideliö
        if root.val > low:
             total += self.rangeSumBST(root.left, low, high)
        
        # Sağ daha büyükse sağa gidelim
        if root.val < high:
            total += self.rangeSumBST(root.right, low, high)
        
        return total
