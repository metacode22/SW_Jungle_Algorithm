import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
top = list(map(int, input().split()))
stack = []
check_list = [0] * n

for idx, x in enumerate(top):
    while stack:
        if stack[-1][1] > x:
            check_list[idx] = stack[-1][0] + 1
            stack.append([idx, x])
            break
        else:
            stack.pop()
        
    if not stack:
        stack.append([idx, x])
            
print(*check_list)
    
    