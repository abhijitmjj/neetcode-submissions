class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(', ']': '[', '}': '{'}

        for elem in s:
            if stack and elem in closeToOpen:
                # we have a non-empty stack and entry is of closing type
                if stack.pop() != closeToOpen[elem]:
                    return False
            else:
                stack.append(elem)
        return len(stack) == 0


        