import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    bracket = list(input().rstrip())
    stack = []
    for i in bracket:
        if i == '(':
            stack.append('(')
        elif i == ')' and stack != []:
            stack.pop()
        elif i == ')' and stack == []:
            stack.append(')')

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')