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
    count = 0
    while left <= right:
        mid = (left + right) // 2
        if cardsA[mid] < num:
            left = mid + 1
        elif cardsA[mid] > num:
            right = mid - 1
        else:
            i, j = 1, 1
            while mid - i >= left:
                if cardsA[mid-i] != cardsA[mid]:
                    break
                else:
                    i += 1
            while mid + j <= right:
                if cardsA[mid+j] != cardsA[mid]:
                    break
                else:
                    j += 1

            count += (i+j - 1)
            left = mid + 1
            break
    return count


for card in cardsB:
    print(binary(card), end=' ')
print()
