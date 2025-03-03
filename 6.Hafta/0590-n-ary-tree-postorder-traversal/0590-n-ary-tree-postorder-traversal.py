"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        
        def traverse(node):
            if not node:
                return
            for child in node.children:
                traverse(child)  # Çocukları ziyaret et
            res.append(node.val)  # Kendi değerini ekle
        
        traverse(root)
        return res
