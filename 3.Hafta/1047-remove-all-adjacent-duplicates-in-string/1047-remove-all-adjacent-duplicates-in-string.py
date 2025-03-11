class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = [0]
        for char in s:
            if char == result[-1]:
                result.pop()
            else:
                result.append(char)
        result.pop(0)
        return "".join(result)
"""
class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = [0]
        for char in s:
            if char == result[-1]:
                result.pop()
            else:
                result.append(char)
        result.pop(0)
        return "".join(result)
        """
