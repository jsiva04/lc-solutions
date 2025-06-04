class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if i == ")":
                    if stack[-1] == "(":
                        stack.pop(len(stack) -1)
                    else:
                        return False
                elif i == "]":
                    if stack[-1] == "[":
                        stack.pop(len(stack) -1)
                    else:
                        return False
                else:
                    if stack[-1] == "{":
                        stack.pop(len(stack) -1)
                    else:
                        return False
        return len(stack) == 0