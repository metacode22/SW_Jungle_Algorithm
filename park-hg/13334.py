import sys
import heapq
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
l = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        a, b = b, a
    l.append([a, b])
l.sort(key=lambda x: (x[-1], x[0]))
d = int(sys.stdin.readline())

ans = 0
heap = []
for a, b in l:
    if b-a <= d:
        heapq.heappush(heap, a)
    else:
        continue

    while heap:
        temp = heap[0]
        if b-temp <= d:
            break
        else:
            heapq.heappop(heap)

    ans = max(ans, len(heap))

print(ans)