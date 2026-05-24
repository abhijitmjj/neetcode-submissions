class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        stack = []

        right = 0

        while right < n:

            # skip multiple slashes
            while right < n and path[right] == '/':
                right += 1
            # start of word boundary
            left = right
            # Move right until the next slash
            while right < n and path[right] != "/":
                right += 1
            pat = path[left:right]
            if pat == "" or pat == ".":
                continue
            if pat == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(pat)
        return "/"+"/".join(stack) 