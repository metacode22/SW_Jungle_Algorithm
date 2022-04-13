import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def max_size():
    stack = []
    max_size = 0
    
    for i in range(n):
        min_point = i
        while stack and stack[-1][0] >= rect[i]:
            h, min_point = stack.pop()
            max_size = max(max_size, h * (i - min_point))
        stack.append([rect[i], min_point])
        
    # if stack:
    #     for _ in stack:
    #         y, x = stack.pop()
    #         max_size = max(max_size, y * (n - x))
    
    for h, point in stack:
        max_size = max(max_size, (n - point) * h)
    
    return max_size
        

while True:
    n, *rect = map(int, input().split())
    
    if n == 0:
        break
    
    print(max_size())