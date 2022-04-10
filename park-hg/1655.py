import sys
import heapq
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
left = []
right = []

for _ in range(N):
    num = int(sys.stdin.readline())

    if len(left) <= len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if left and right and -left[0] > right[0]:
        l, r = heapq.heappop(left), heapq.heappop(right)
        heapq.heappush(left, -r)
        heapq.heappush(right, -l)

    print(-left[0])