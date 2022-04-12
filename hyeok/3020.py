# 너무 어려워요 ㅠ
import sys

sys.stdin = open("input_py.txt")

input = sys.stdin.readline

N, H = map(int, input().split())

up = []
down = []

for i in range(N):
    x = int(input())
    if i % 2 == 0:
        up.append(x)
    else:
        down.append(x)

# up down 둘 다 들어와야 하기 때문에 Parameter로 arr을 받아야함
# 마찬가지로 up down 시작점과 끝점 (left, right)과 target이 다르기 때문에
# Parameter로 받아줘야함


def binary(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


minCnt = N
rangeCnt = 0


def search():
    global rangeCnt, minCnt
    for i in range(1, H+1):
        downCnt = len(down) - binary(down, i - 0.5, 0, len(down) - 1)
        upCnt = len(up) - binary(up, h - i + 0.5, 0, len(up) - 1)

        if minCnt == downCnt + upCnt:
            rangeCnt += 1
        elif minCnt > downCnt + upCnt:
            rangeCnt = 1
            minCnt = downCnt + upCnt


print(minCnt, rangeCnt)
