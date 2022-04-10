import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque(range(1, n + 1))
check_list = []

cnt = 0
while len(queue) > 0:
    cnt += 1

    if cnt != k:
        queue.append(queue.popleft())
    elif cnt == k:
        check_list.append(queue.popleft())
        cnt = 0

print('<', end='')
print(*check_list, sep=', ', end='')
print('>', end='')