import sys

input = sys.stdin.readline

K = int(input())

stack = []

for i in range(K):
    money = int(input().strip())
    if money == 0:
        stack.pop()
    else:
        stack.append(money)


print(sum(stack))
