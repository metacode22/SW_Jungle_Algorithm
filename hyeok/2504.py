import sys
sys.stdin = open("./input_py.txt", "r")
input = sys.stdin.readline

brackets = input().strip()

stack = []

lengthB = len(brackets)
tmp = 1

answer = 0

for i in range(lengthB):
    if brackets[i] == "(":
        tmp *= 2
        stack.append("(")
    elif brackets[i] == "[":
        tmp *= 3
        stack.append("[")
    elif brackets[i] == ")":
        if stack[-1] == "[" or not stack:
            answer = 0
            break
        if brackets[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if brackets[i-1] == "[":
            answer += tmp
        stack.pop()
        tmp //= 3

print(answer)


# value = 0

# square = []

# parentheses = []

# tmp = 1

# lengthB = len(brackets)

# # (2) [3] 틀렸다 븅신아
# for i in range(lengthB):
#     if brackets[i] == "(":
#         parentheses.append(2)
#         tmp *= 2
#     elif brackets[i] == "[":
#         square.append(3)
#         tmp *= 3
#     elif brackets[i] == "]":
#         if not square or parentheses:
#             value = 0
#             # print("@#")
#             break
#         value += tmp
#         square.pop()
#         tmp //= 3
#     else:
#         if not parentheses or square:
#             value = 0
#             # print("@#@")
#             break
#         value += tmp
#         parentheses.pop()
#         tmp //= 2


# print(value)
