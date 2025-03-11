class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        
        num_stack = []
        op_stack = []

        for char in s:
            if char.isdigit():
                num_stack.append(int(char))
            else:
                op_stack.append(char)

        i = 0
        while i < len(op_stack):
            if op_stack[i] in "*/":
                if op_stack[i] == "*":
                    num_stack[i] *= num_stack[i + 1]
                else:
                    num_stack[i] //= num_stack[i + 1]  # Tam sayı bölme
                num_stack.pop(i + 1)
                op_stack.pop(i)
            else:
                i += 1

        i = 0
        while i < len(op_stack):
            if op_stack[i] == "+":
                num_stack[i] += num_stack[i + 1]
            else:
                num_stack[i] -= num_stack[i + 1]
            num_stack.pop(i + 1)
            op_stack.pop(i)

        return num_stack[0]
