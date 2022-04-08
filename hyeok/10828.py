import sys

input = sys.stdin.readline

N = int(input())
commands = [input().strip() for _ in range(N)]

stack = []

for command in commands:
    lengthS = len(stack)
    if command == 'top':
        if lengthS == 0:
            print("-1")
        else:
            print(stack[-1])
    elif command == "size":
        print(lengthS)
    elif command == "empty":
        if lengthS == 0:
            print("1")
        else:
            print("0")
    elif command == "pop":
        if lengthS == 0:
            print("-1")
        else:
            print(stack.pop())
    else:
        stack.append(command.split()[1])

# print(commands)
