import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    x = int(input())
    
    if x == 0:
        if not a:
            print(0)
        else:
            print(-heapq.heappop(a))
    
    else:
        heapq.heappush(a, -x)        
    