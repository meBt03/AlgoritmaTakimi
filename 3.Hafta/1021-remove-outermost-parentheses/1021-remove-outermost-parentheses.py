class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        sayaç = 0
        for char in s:
            if char == '(':
                if sayaç > 0:
                    result.append(char)
                sayaç += 1
            else:
                sayaç -=1           
                if sayaç > 0:
                    result.append(char)
                
        
        return "".join(result)
