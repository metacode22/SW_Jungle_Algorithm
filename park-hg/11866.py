import sys
from collections import deque
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())

que = deque(range(1, N+1))
ans = []

cnt = 1
while que:
    num = que.popleft()
    if cnt%K == 0:
        ans.append(str(num))
    else:
        que.append(num)
    cnt += 1

print("<" + ", ".join(ans)+">")