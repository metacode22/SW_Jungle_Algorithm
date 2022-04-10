# 다시풀기
# good
import sys
import heapq

# sys.stdin = open("input_py.txt")
input = sys.stdin.readline

n = int(input())

road_info = [[int(x) for x in input().split()]for i in range(n)]

d = int(input())

####
roads = []
for road in road_info:
    x, y = road
    if abs(x - y) <= d:
        if x > y:
            roads.append([y, x])
        else:
            roads.append([x, y])
        # road = sorted(road)
        # roads.append(road)

roads.sort(key=lambda x: x[1])
# print(roads) 뒤에만 정렬됨 ... 왜...? 이렇게 해도 되나 ?
answer = 0
heap = []
for road in roads:
    if not heap:
        heapq.heappush(heap, road)
    else:
        while heap[0][0] < road[1]-d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, road)
    answer = max(answer, len(heap))
print(answer)
# python sort : O(nlogN) // heap sort : O(nlogN)
# homeOffice = []
# for i in range(n):
#     x, y = map(int, input().split())
#     if x > y:
#         homeOffice.append([y, x])
#     else:
#         homeOffice.append([x, y])
# d = int(input())

# # print(homeOffice)
# homeOffice.sort(key=lambda x: (x[0], x[1]))

# heap = []
# for i in range(n):
#     if abs(homeOffice[i][0] - homeOffice[i][1]) > d:
#         continue
#     heapq.heappush(heap, (homeOffice[i][0], homeOffice[i][1]))

# maxN = 0


# # print(heap)
# while True:
#     if maxN >= len(heap):
#         break
#     count = 1
#     # start = heap[0]
#     train = heapq.heappop(heap)
#     # start = train[0]
#     end = traind[0] + d
#     for i in range(len(heap)):
#         if heap[i][1] <= end:
#             count += 1
#             continue
#         break
#     # maxN = count if maxN < count else maxN
#     maxN = max(count, maxN)


# # print(homeOffice)
# print(maxN)
