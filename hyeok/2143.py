# wrong code - binary search -- fuck
# import sys

# sys.stdin = open("input_py.txt")

# input = sys.stdin.readline


# def binary():
#     answer = []
#     for suma in sumA:
#         if suma >= T:
#             continue
#         count = 0
#         left = 0
#         right = len(sumB) - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if sumB[mid] <= T-suma:
#                 left = mid + 1
#                 # if sumB[mid] == T-suma :

#             else:
#                 right = mid - 1
#         answer.append(left-1)
#     return answer


# T = int(input())

# n = int(input())

# A = [int(x) for x in input().split()]

# m = int(input())

# B = [int(x) for x in input().split()]

# sumA = []
# sumB = []

# for i in range(n):
#     s = A[i]
#     sumA.append(s)
#     for j in range(i+1, n):
#         s += A[j]
#         sumA.append(s)

# sumA.sort()

# for i in range(m):
#     s = B[i]
#     sumB.append(s)
#     for j in range(i+1, m):
#         s += B[j]
#         sumB.append(s)

# sumB.sort()

# print(sumA)
# print(sumB)

# print(binary())
# print(sum(binary()))
