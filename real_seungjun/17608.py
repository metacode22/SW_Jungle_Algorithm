import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input())
stack = []
for _ in range(t):
    n = int(input())
    stack.append(n)

first = stack[-1]
cnt = 0
for i in range(len(stack) - 2, -1, -1):
    if stack[i] > first:
        cnt += 1
        first = stack[i]

print(cnt + 1)