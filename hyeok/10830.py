import sys

input = sys.stdin.readline

N, B = map(int, input().split())

matrix = [[int(x) for x in input().split()] for _ in range(N)]


def multi(arr1, arr2):
    squared = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for i in range(N):
                squared[x][y] += arr1[x][i] * arr2[i][y]
    return squared


def dc(arr, divide):
    if divide == 1:
        return remain(arr)
    else:
        tmp = dc(arr, divide//2)
        if divide % 2 == 0:
            return remain(multi(tmp, tmp))
        else:
            return remain(multi(multi(tmp, tmp), arr))


def remain(arr):
    for x in range(N):
        for y in range(N):
            arr[x][y] %= 1000
    return arr


# print(matrix)
# matrix = map(remain, matrix[0])
# print(remain(matrix))

# print(dc(matrix, B))

answer = dc(matrix, B)

# 더 좋은 출력 방법 없을까 ?
for i in answer:
    for j in i:
        print(j, end=' ')
    print()
