import sys

input = sys.stdin.readline

N = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(N)]

blue, white = 0, 0


def find(N, arr, x, y):
    # global blue, white
    if N == 1:
        blueAndWhite(arr, x, y)
        return
    if check(N, arr, x, y):
        blueAndWhite(arr, x, y)
    else:
        N //= 2
        find(N, arr, x, y)
        find(N, arr, x+N, y)
        find(N, arr, x, y+N)
        find(N, arr, x+N, y+N)


def blueAndWhite(arr, x, y):
    global blue, white
    if arr[x][y] == 0:
        white += 1
    else:
        blue += 1


def check(N, arr, x, y):
    stand = arr[x][y]
    for i in range(N):
        for j in range(N):
            if stand != arr[x+i][y+j]:
                return False
    return True


# print(matrix)

find(N, matrix, 0, 0)
print(f"{white}\n{blue}")
# print(white)
# print(blue)
# 속도 비슷하다.
# sys.stdout.write("%s\n" % white)
# sys.stdout.write("%s" % blue)
