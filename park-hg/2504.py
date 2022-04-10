import sys
sys.stdin = open('input.txt')

pars = list(sys.stdin.readline().rstrip())

stack = []
for par in pars:
    if par == '(':
        stack.append('(')
    elif par == '[':
        stack.append('[')

    elif par == ')':
        if stack:
            if stack[-1] == '(':
                stack.pop()
                stack.append(2)
            else:
                if isinstance(stack[-1], int) and stack[-2] == '(':
                    v = stack.pop()
                    stack.pop()
                    stack.append(v*2)
                else:
                    stack.append(')')
        else:
            stack.append(')')

    elif par == ']':
        if stack:
            if stack[-1] == '[':
                stack.pop()
                stack.append(3)
            else:
                if isinstance(stack[-1], int) and stack[-2] == '[':
                    w = stack.pop()
                    stack.pop()
                    stack.append(w*3)
                else:
                    stack.append(']')
        else:
            stack.append(']')
    temp = 0
    while stack and isinstance(stack[-1], int):
        v = stack.pop()
        temp += v
    if temp != 0:
        stack.append(temp)

if len(stack) == 1 and isinstance(stack[-1], int):
    print(stack[-1])
else:
    print(0)