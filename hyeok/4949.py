import sys

sys.stdin = open("input_py.txt")
input = sys.stdin.readline

answer = []

while True:
    sentence = input()
    if sentence == '.':
        break
    stack = []
    tmp = True
    for i in range(len(sentence)):
        # print(sentence[i])
        if sentence[i] == "[" or sentence[i] == "(":
            stack.append(sentence[i])
        elif sentence[i] == "]":
            if not stack or stack[-1] != "[":
                # answer.append("no")
                tmp = False
                break
            elif stack[-1] == "[":
                stack.pop()
        elif sentence[i] == ")":
            if not stack or stack[-1] != "(":
                # answer.append("no")
                tmp = False
                break
            elif stack[-1] == "(":
                stack.pop()
    if tmp == True and len(stack) == 0:
        print("yes")
    else:
        print("no")


# print(*answer)
