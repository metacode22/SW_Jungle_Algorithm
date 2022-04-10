import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))

ans = []
stack = []
for i, h in enumerate(towers):
    if not stack:
        ans.append(0)
    else:
        if stack[-1][1] > h:
            ans.append(stack[-1][0])
        else:
            while stack:
                if stack[-1][1] > h:
                    break
                stack.pop()
            if not stack:
                ans.append(0)
            else:
                ans.append(stack[-1][0])
                
    stack.append((i+1, h))

print(*ans)