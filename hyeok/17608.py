# 내꺼
# import sys

# input = sys.stdin.readline

# N = int(input())

# sticks = [int(input()) for _ in range(N)]


# # print(sticks)

# standard = sticks.pop()
# count = 1
# for _ in range(N-1):
#     comp = sticks.pop()
#     if standard < comp:
#         count += 1
#         standard = comp

# print(count)

# 동규쿤
import sys

sys.stdin = open("input_py.txt")
input = sys.stdin.readline

N = int(input())
stick = []
count = 1
for _ in range(N):
    stick.append(int(input()))

for i in range(0, N):
    if stick[i] == stick[-1]:
        count += 0
    elif stick[i] >= stick[-1]:
        count += 1
print(count)
