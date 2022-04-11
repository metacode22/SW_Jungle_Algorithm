import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
    cmd = int(input())

    if cmd == 0:
        if len(a) == 0:
            print(0)
        else:
            print(abs(heapq.heappop(a)))

    else:
        heapq.heappush(a, -cmd)