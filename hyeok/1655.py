import sys
import heapq

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline


N = int(input())

leftHeap = []
rightheap = []

answer = []

for i in range(N):
    inputN = int(input())

    if len(leftHeap) == len(rightheap):
        heapq.heappush(leftHeap, (-inputN, inputN))
    else:
        heapq.heappush(rightheap, (inputN, inputN))
    if rightheap and leftHeap[0][1] > rightheap[0][0]:
        min = heapq.heappop(rightheap)[0]
        max = heapq.heappop(leftHeap)[1]
        heapq.heappush(leftHeap, (-min, min))
        heapq.heappush(rightheap, (max, max))

    answer.append(leftHeap[0][1])
for i in answer:
    print(i)
