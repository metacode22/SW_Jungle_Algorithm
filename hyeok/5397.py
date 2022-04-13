import sys

# sys.stdin = open("input_py.txt")
input = sys.stdin.readline

N = int(input())


def loger(string):
    stack = []
    tmp = []
    lengthS = len(string)
    for i in range(lengthS):
        if string[i] == "<":
            if stack:
                tmp.append(stack.pop())
        elif string[i] == ">":
            if tmp:
                stack.append(tmp.pop())
        elif string[i] == "-":
            if stack:
                stack.pop()
        else:
            stack.append(string[i])

    while tmp:
        stack.append(tmp.pop())
    return stack


answer = []

for i in range(N):
    keys = input().strip()
    # print(* loger(keys), sep='')
    answer.append(loger(keys))

for ans in answer:
    print(*ans, sep='')
