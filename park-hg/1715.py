import sys
import heapq
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    heapq.heappush(heap, x)

ans = 0
while len(heap) > 1:
    a, b = heapq.heappop(heap), heapq.heappop(heap)
    ans += (a+b)
    heapq.heappush(heap, a+b)

print(ans)