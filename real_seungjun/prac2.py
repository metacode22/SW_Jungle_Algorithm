import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

a = []

heapq.heappush(a, 1)
heapq.heappush(a, 5)
heapq.heappush(a, 3)
heapq.heappush(a, 0)

print(a)