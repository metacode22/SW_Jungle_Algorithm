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


import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))

    # Set sums
    a_sums = {}
    for i in range(n):
        cur_sum = 0
        for j in range(i, n):
            cur_sum += A[j]

            if a_sums.get(cur_sum):
                a_sums[cur_sum] += 1
            else:
                a_sums[cur_sum] = 1

    b_sums = {}
    for i in range(m):
        cur_sum = 0
        for j in range(i, m):
            cur_sum += B[j]

            if b_sums.get(cur_sum):
                b_sums[cur_sum] += 1
            else:
                b_sums[cur_sum] = 1

    # Solution
    count = 0
    for k, v in a_sums.items():
        if b_sums.get(T-k):
            count += v*b_sums[T-k]

    print(count)
