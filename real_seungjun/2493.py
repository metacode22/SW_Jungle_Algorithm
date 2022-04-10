import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
top = list(map(int, input().split()))
stack = []
res = [0] * n

for i in range(n):
    if stack:
        while stack:
            if stack[-1][1] <= top[i]:
                stack.pop()
            else:
                res[i] = stack[-1][0] + 1
                break
        stack.append([i, top[i]])
    else:
        stack.append([i, top[i]])
        res[i] = 0

print(*res)