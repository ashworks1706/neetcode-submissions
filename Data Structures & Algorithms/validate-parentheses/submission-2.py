class Solution:
    def isValid(self, s: str) -> bool:
        comp = {"{": "}", "[": "]", "(": ")"}
        stack = []

        for char in s:
            if char in comp:  
                stack.append(char)
            elif char in comp.values():
                if not stack or comp[stack.pop()] != char:
                    return False

        return len(stack) == 0
