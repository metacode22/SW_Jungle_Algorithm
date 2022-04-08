# i don'y Know
import sys

sys.stdin = open("./input_py.txt", "r")
input = sys.stdin.readline

# 이게 이진탐색 ... ?

M, N, L = map(int, input().split())

shooters = [int(x) for x in input().split()]

targets = [[int(x) for x in input().split()] for _ in range(N)]

flag = [False] * N

# arr : targets, location : shooters location,


# def shoot(arr, location):
#     for x in range(N):
#         for y in range(2):
#             arr[x][y]


#     return


print(targets)
