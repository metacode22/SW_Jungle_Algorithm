import sys
import heapq

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N = int(input())

heap = []

for i in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-x, x))
