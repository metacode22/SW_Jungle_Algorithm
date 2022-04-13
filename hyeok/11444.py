import sys

sys.stdin = open("input_py.txt")
input = sys.stdin.readline

N = int(input())

fibomat = [[1, 1], [1, 0]]


def matrix(nums, arr):
    if nums == 1:
        return remain(arr)
    tmp = matrix(nums//2, arr)
    if nums % 2 == 0:
        return remain(multi(tmp, tmp))
    else:
        return remain(multi(multi(tmp, tmp), arr))


def multi(arr1, arr2):
    answer = [[0, 0], [0, 0]]
    for x in range(2):
        for y in range(2):
            for i in range(2):
                answer[x][y] += arr1[x][i] * arr2[i][y]
    return answer


def remain(arr):
    for i in range(2):
        for j in range(2):
            arr[i][j] %= 1000000007
    return arr


# tmp = matrix(N-1, fibomat)


if N < 3:
    print(1)
else:
    print(matrix(N-1, fibomat)[0][0])
# answer = tmp[0][0] + tmp[1][0]
