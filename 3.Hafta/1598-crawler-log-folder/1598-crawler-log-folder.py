class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for order in logs:
            if order == "../":
                if count > 0:
                    count -= 1
            elif order == "./":
                count += 0
            else:
                count += 1
            
        return count

"""
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        history = []
        count = 0
        for order in logs:
            if order == "../":
                if history:
                    history.pop()
                    count -= 1
            elif order == "./":
                continue
            else:
                history.append(order)
                count += 1
            
        return count
"""
