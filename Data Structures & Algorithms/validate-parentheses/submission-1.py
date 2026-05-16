class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', '}': '{', ']': '[' }
        if len(s) == 0:
            return True
        for elem in s:
            if elem in [x for x in matching.values()]:
                stack.append(elem)
                
            if elem in matching:
                if stack and stack[-1] == matching[elem]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

            


        