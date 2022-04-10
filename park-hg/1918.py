import sys
sys.stdin = open('input.txt')

temp = list(sys.stdin.readline().rstrip())
stack = []
ans = ''

for t in temp:

    if t in ["+", "-"]:
        while stack and stack[-1] in ["+", "-", "*", "/"]:
            ans += stack.pop()
        stack.append(t)

    elif t in ["*", "/"]:
        while stack and stack[-1] in ["*", "/"]:
            ans += stack.pop()
        stack.append(t)

    elif t == "(":
        stack.append(t)

    elif t == ")":
        while stack and stack[-1] != "(":
            ans += stack.pop()
        if stack[-1] == "(":
            stack.pop()
    else:
        ans += t

while stack:
    ans += stack.pop()

print(ans)
    