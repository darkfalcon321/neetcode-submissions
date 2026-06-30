class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {")": "(", "}": "{", "]": "["}

        stack = []
        for par in s:
            if par in parenthesis: #check if its key
                if not stack or stack.pop() != parenthesis[par]:
                    return False
            else:
                stack.append(par)

        if stack:
            return False
        else:
            return True
