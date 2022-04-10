import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for _ in range(T):
    pars = list(sys.stdin.readline().rstrip())
    stack = []
    for par in pars:
        if par == '(':
            stack.append('(')
        elif par == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')