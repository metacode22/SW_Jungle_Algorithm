import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
k = int(input())
mat = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    mat[x - 1][y - 1] = 2
l = int(input())
direction_dict = dict()
for _ in range(l):
    x, y = map(str, input().rstrip().split())
    direction_dict[int(x)] = y

def turn(direction, time):
    if direction_dict[time] == 'L':
        direction = (direction - 1) % 4
    # direction_dict[time] == 'D' 일때
    else:
        direction = (direction + 1) % 4
    return direction
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

direction = 1
time = 0
x, y = 0, 0
mat[x][y] = 1
visited = deque()
visited.append([x, y])

while True:
    time += 1
    x += dx[direction]
    y += dy[direction]
    
    if x < 0 or x >= n or y < 0 or y >= n:
        break
    
    if mat[x][y] == 2:
        mat[x][y] = 1
        visited.append([x, y])
        if time in direction_dict:
            direction = turn(direction, time)
            
    elif mat[x][y] == 0:
        mat[x][y] = 1
        visited.append([x, y])
        front_x, front_y = visited.popleft()
        mat[front_x][front_y] = 0
        if time in direction_dict:
            direction = turn(direction, time)
    
    # mat[x][y] == 1, 즉 자신의 몸을 만난 경우        
    else:
        break
    
print(time)