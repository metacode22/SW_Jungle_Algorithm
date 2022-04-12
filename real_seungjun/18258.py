import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

queue = deque()

def push(x):
    queue.append(x)
    
def remove():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.popleft())
        
def size():
    print(len(queue))

def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)
        
def front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])
    
def back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])
    
n = int(input())
for _ in range(n):
    cmd = list(input().split())
    
    if cmd[0] == 'push':
        push(int(cmd[1]))
        
    if cmd[0] == 'pop':
        remove()
        
    if cmd[0] == 'size':
        size()
        
    if cmd[0] == 'empty':
        empty()
        
    if cmd[0] == 'front':
        front()
        
    if cmd[0] == 'back':
        back()
    