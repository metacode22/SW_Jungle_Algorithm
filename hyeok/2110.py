import sys

input = sys.stdin.readline

N, C = map(int, input().split())

homes = [int(input()) for i in range(N)]

homes.sort()


print(homes)


def install(arr, left, right):
    midV = (arr[left] + arr[right]) // N
    if midV > arr[(left+right)//N]:
        return

################
# # 적당히 설치 .... ?
# i don't know
