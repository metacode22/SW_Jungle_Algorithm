from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

yosep = deque(i+1 for i in range(N))

answer = []

# print(yosep.popleft())

while len(yosep) > 0:
    # if len(yosep) == 1:
    #     answer.append(yosep.pop())
    #     break
    for i in range(K-1):
        # tmp = yosep.popleft()
        yosep.append(yosep.popleft())
    answer.append(yosep.popleft())

print("<", end='')
# print(', '.join(map(str, answer)), end='')
print(*answer, sep=', ', end='')
print(">")
