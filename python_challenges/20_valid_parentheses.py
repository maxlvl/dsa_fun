# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


class Solution:
    def isValid(self, strang: str) -> bool:
        stack = []
        for ch in strang:
            match ch:
                case ")":
                    if stack and stack[-1] == "(":
                        stack.pop()
                    else:
                        stack.append(ch)
                case "]":
                    if stack and stack[-1] == "[":
                        stack.pop()
                    else:
                        stack.append(ch)
                case "}":
                    if stack and stack[-1] == "{":
                        stack.pop()
                    else:
                        stack.append(ch)
                case other:
                    stack.append(ch)
        return not stack


def test_solution():
    assert Solution().isValid("()") == True
    assert Solution().isValid("()[]{}") == True
    assert Solution().isValid("(]") == False
    assert Solution().isValid("([)]") == False
