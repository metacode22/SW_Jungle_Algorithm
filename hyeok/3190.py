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
            cur_d = (cur_d+moves[t]) % 4


print(snake_move())

# import sys
# from collections import deque

# sys.stdin = open("input_py.txt")
# input = sys.stdin.readline

# # 상 우 하 좌
# dy = [0, 1, 0, -1]
# dx = [-1, 0, 1, 0]


# def change(d, c):
#     if c == "L":
#         d = (d-1) % 4
#     else:
#         d = (d+1) % 4
#     return d


# def game():
#     direction = 1
#     time = 1
#     x, y = 0, 0
#     visited = deque([[x, y]])
#     arr[x][y] = 2
#     while True:
#         x, y = x + dx[direction], y+dy[direction]
#         if 0 <= x < N and 0 <= y < N and arr[x][y] != 2:
#             if not arr[x][y] == 1:
#                 temp_x, temp_y = visited.popleft()
#                 arr[temp_x][temp_y] = 0  # remove tail
#             arr[x][y] = 2
#             visited.append([x, y])
#             if time in chances.keys():
#                 direction = change(direction, chances[time])
#             time += 1
#         else:
#             return time


# # N :size of board
# N = int(input())
# arr = [[0]*N for i in range(N)]
# # K : amount of apples
# K = int(input())

# # apples = 1
# for i in range(K):
#     x, y = map(int, input().split())
#     arr[x-1][y-1] = 1

# # amount of direction chances
# L = int(input())
# chances = {}
# for i in range(L):
#     time, direction = input().split()
#     chances[int(time)] = direction

# print(game())
