# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            match token:
                case "+":
                    rhs = int(stack.pop())
                    lhs = int(stack.pop())
                    stack.append(lhs + rhs)
                case "-":
                    rhs = int(stack.pop())
                    lhs = int(stack.pop())
                    stack.append(lhs - rhs)
                case "*":
                    rhs = int(stack.pop())
                    lhs = int(stack.pop())
                    stack.append(lhs * rhs)
                case "/":
                    rhs = int(stack.pop())
                    lhs = int(stack.pop())
                    stack.append(lhs / rhs)
                case _:
                    stack.append(token)

        return int(stack[0])
