import sys

input = sys.stdin.readline

N = int(input())

A = [int(x) for x in input().split()]

A.sort()

M = int(input())

Am = [int(x) for x in input().split()]

# 시간초과
# for num in Am:
#     if num in A:
#         print("1")
#     else:
#         print("0")


def binarySearch(start, end, arr, find):
    if start > end:
        return 0
    mid = (start+end)//2
    if arr[mid] == find:
        return 1
    elif arr[mid] > find:
        return binarySearch(start, mid-1, arr, find)
    else:
        return binarySearch(mid+1, end, arr, find)


for num in Am:
    print(binarySearch(0, N-1, A, num))
