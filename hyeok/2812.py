# T _ T
import sys

# sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())

nums = list(map(int, input().strip()))
stack = []

for num in nums:
    while stack and stack[-1] < num and K > 0:
        stack.pop()
        K -= 1
    stack.append(num)

while K > 0:
    stack.pop()
    K -= 1

print(''.join(stack))
