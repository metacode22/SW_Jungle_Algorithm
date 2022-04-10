import sys
import heapq


sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline
N = int(input())

cards = []

for i in range(N):
    x = int(input())
    heapq.heappush(cards, x)

# print(cards[0])
answer = 0
for i in range(N-1):
    minNumF = heapq.heappop(cards)
    minNumS = heapq.heappop(cards)
    heapq.heappush(cards, minNumF+minNumS)
    answer += minNumS + minNumF

print(answer)
