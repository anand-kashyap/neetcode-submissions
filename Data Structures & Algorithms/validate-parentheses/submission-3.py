class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        for c in s:
            if c in brackets:
                stack.append(brackets[c])
            else:
                if not stack or stack[-1] != c:
                    return False
                stack.pop()
        if not stack:
            return True
        return False