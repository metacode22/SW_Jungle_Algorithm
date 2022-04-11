import sys
from collections import deque

sys.stdin = open("input_py.txt")
input = sys.stdin.readline


def bfs(mid):
    visit[i1] = 1
    q = deque()
    q.append(i1)
    while q:
        start = q.popleft()
        if start == i2:
            return True
        for nx, nc in s[start]:
            if visit[nx] == 0 and mid <= nc:
                q.append(nx)
                visit[nx] = 1
    return False


N, M = map(int, input().split())

s = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    s[a].append([b, c])
    s[b].append([a, c])

i1, i2 = map(int, input().split())

left, right = 0, 10**9+1

while left < right:
    visit = [0 for _ in range(N+1)]
    mid = (left + right) // 2
    if bfs(mid):
        left = mid + 1
    else:
        right = mid

print(left - 1)
