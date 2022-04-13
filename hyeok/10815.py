import sys

sys.stdin = open("input_py.txt")

input = sys.stdin.readline

N = int(input())

cardsA = [int(x) for x in input().split()]

cardsA.sort()

M = int(input())

cardsB = [int(x) for x in input().split()]


def binary(num):
    left = 0
    right = len(cardsA) - 1
    result = 0
    # print(cardsA[(left+right)//2])
    while left <= right:
        mid = (left + right) // 2
        if cardsA[mid] < num:
            left = mid+1
        elif cardsA[mid] > num:
            right = mid - 1
        else:
            result = 1
            break
    return result


for cardB in cardsB:
    # print(cardB)
    print(binary(cardB), end=' ')
print()
# time over
# for cardB in cardsB:
#     if cardB in cardsA:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')
# print()
