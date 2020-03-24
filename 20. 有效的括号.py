class Solution:
    """
    https://leetcode-cn.com/problems/valid-parentheses/
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

    有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    注意空字符串可被认为是有效字符串。
    """

    def __init__(self):
        self.bracket_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

    def isValid(self, s: str) -> bool:
        if not s or len(s) == 0:
            return True

        stack = []
        for item in s:
            # 如果遇到了右括号，就弹出栈顶，如果匹配则扔掉，不匹配则返回false
            if item in self.bracket_map:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if self.bracket_map[item] != top:
                    return False

            # 如果遇到了左括号，则入栈
            if item in self.bracket_map.values():
                stack.append(item)

        if len(stack) > 0:
            return False

        return True


s = Solution()
#s.isValid("([)]")
s.isValid("]")
