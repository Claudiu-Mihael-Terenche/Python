# 224. Basic calculator https://leetcode.com/problems/basic-calculator/
# Claudiu Mihael Terenche, 6268599, FSD 10, 22.12.2023
"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it,
and return the result of the evaluation.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
such as eval().
Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""
# driver code
str1 = '(1+(4+5+2)-3)+(6+8)'


def calculate(str1):
    stack = []
    operand = 0
    result = 0  # For the final result
    sign = 1  # 1 represents positive sign, -1 represents negative sign

    for char in str1:
        if char.isdigit():
            operand = operand * 10 + int(char)
        elif char == '+':
            result += sign * operand
            sign = 1
            operand = 0
        elif char == '-':
            result += sign * operand
            sign = -1
            operand = 0
        elif char == '(':
            stack.append((result, sign))
            result = 0
            sign = 1
        elif char == ')':
            result += sign * operand
            prev_result, prev_sign = stack.pop()
            result = prev_result + prev_sign * result
            operand = 0

    return result + sign * operand



result = calculate(str1)
print(result)
