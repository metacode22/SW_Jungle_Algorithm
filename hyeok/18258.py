
import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())

# for i in range(n):
#   commands = int(input().strip())
commands = [input().strip() for _ in range(n)]

queue = deque([])

length = len(queue)

for command in commands:
    # pop
    if command == 'pop':
        if length == 0:
            print("-1")
        else:
            print(queue.pop())
            length -= 1
    # size
    elif command == 'size':
        print(length)
        # print(len(queue))
    # empty
    elif command == 'empty':
        if length:
            print("0")
        else:
            print("1")
    # front
    elif command == 'front':
        if length == 0:
            print("-1")
        else:
            print(queue[length-1])
    # back
    elif command == 'back':
        if length == 0:
            print("-1")
        else:
            print(queue[0])
    # push X
    else:
        num = list(command.split())[1]
        queue.appendleft(num)
        length += 1
