import sys
input = sys.stdin.readline
n, k = map(int, input().split())
num = list(map(int, list(str(input().rstrip()))))

stack = []
cnt = 0

for i in range(n):
    while stack and stack[-1] < num[i] and cnt < k:
        stack.pop()
        cnt += 1
    stack.append(num[i])
    
if cnt < k:
    print(''.join(map(str, stack[:-(k - cnt)])))
else:
    print(''.join(map(str, stack)))