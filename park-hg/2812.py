import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
nums = list(sys.stdin.readline().rstrip())
stack = []

for num in nums:
    while stack and stack[-1] < num and K > 0:
        stack.pop()
        K -= 1
    stack.append(num)

while K > 0:
    stack.pop()
    K -= 1
print(stack)
print(''.join(stack))
