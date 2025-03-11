class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        order = []
        target_index = 0
        for i in range(1, n+1):
            stack.append(i)
            order.append("Push")

            if stack[-1] == target[target_index]:
                target_index += 1                
            else:
                stack.pop()
                order.append("Pop")
            if target_index == len(target):
                break
        
        return order

