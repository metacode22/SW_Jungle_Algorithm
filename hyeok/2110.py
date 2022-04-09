# 다시 풀기
import sys

input = sys.stdin.readline

N, C = map(int, input().split())

homes = [int(input()) for i in range(N)]

homes.sort()
# 사이값
# start = 1
# end = homes[-1] - homes[0]


def install(arr, start, end):
    global answer
    while start <= end:
        mid = (start + end) // 2
        current = arr[0]
        count = 1

        for i in range(1, len(arr)):
            if arr[i] >= current + mid:
                count += 1
                current = arr[i]
        if count >= C:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


install(homes, 1,  homes[-1] - homes[0])
print(answer)
