import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

queue = deque(range(1, n + 1))

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
    
print(queue[0])