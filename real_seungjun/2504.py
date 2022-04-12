import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

bracket = list(input().rstrip())
stack = []
tmp = 1
res = 0

for i in range(len(bracket)):
    if bracket[i] == '(':
        stack.append(bracket[i])
        tmp *= 2
        
    elif bracket[i] == '[':
        stack.append(bracket[i])
        tmp *= 3
        
    elif bracket[i] == ')':
        if not stack or stack[-1] == '[':       # stack에 아무것도 없거나, 전에 원소가 잘못된 원소라면
            res = 0
            break
        elif bracket[i - 1] == '(':             # 1번만 결과에 더해질 수 있도록
            res += tmp
        tmp //= 2
        stack.pop()
    
    elif bracket[i] == ']':
        if not stack or stack[-1] == '(':       # stack에 아무것도 없거나, 전에 원소가 잘못된 원소라면
            res = 0
            break
        elif bracket[i - 1] == '[':             # 1번만 결과에 더해질 수 있도록
            res += tmp
        tmp //= 3
        stack.pop()
        
if stack:       # stack에 원소가 남아 있다면 잘못된 결과
    print(0)
else:
    print(res)