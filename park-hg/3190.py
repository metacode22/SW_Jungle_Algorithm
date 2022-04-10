import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
grid = [[0]*N for _ in range(N)]

K = int(sys.stdin.readline())
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    grid[a-1][b-1] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
L = int(sys.stdin.readline())
moves = {}
for _ in range(L):
    a, b = sys.stdin.readline().split()
    if b == "L":
        moves[int(a)] = -1
    elif b == "D":
        moves[int(a)] = 1

snake = deque([[0, 0]])


def snake_move():
    t = 0
    cur_d = 1
    
    while True:
        x, y = snake[-1]
        nx, ny = x+dx[cur_d], y+dy[cur_d]
        t += 1

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return t

        if [nx, ny] in snake:
            return t

        snake.append([nx, ny])

        if grid[nx][ny] == 1:
            grid[nx][ny] = 0
        else:
            snake.popleft()

        if t in moves:
            cur_d = (cur_d+moves[t])%4

print(snake_move())
