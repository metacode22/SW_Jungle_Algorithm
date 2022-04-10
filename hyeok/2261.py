# 다시 풀기
# FUCK YOU
import sys

sys.stdin = open("input_py.txt")
input = sys.stdin.readline

n = int(input())

coordinate = [[int(x) for x in input().split()] for i in range(n)]

# coordinate.sort(key=lambda x: x[0])
coordinate.sort()
# print(f"coordinate : {coordinate}")


def distance(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2


def dac(start, end):
    if start == end:
        return float('inf')

    if end - start == 1:
        return distance(coordinate[start], coordinate[end])

    # divide & conquer
    mid = (start + end) // 2
    minDist = min(dac(start, mid), dac(mid, end))

    # x축을 기준으로 후보점 find
    target_coordinate = []
    for i in range(start, end+1):
        if(coordinate[mid][0] - coordinate[i][0])**2 < minDist:
            target_coordinate.append(coordinate[i])

    # y축 정렬
    target_coordinate.sort(key=lambda x: x[1])

    # y축을 기준으로 후보점 find
    t = len(target_coordinate)
    for i in range(t-1):
        for j in range(i+1, t):
            if (target_coordinate[i][1] - target_coordinate[j][1])**2 < minDist:
                minDist = min(minDist, distance(
                    target_coordinate[i], target_coordinate[j]))
            else:
                break
    return minDist


print(dac(0, n-1))
