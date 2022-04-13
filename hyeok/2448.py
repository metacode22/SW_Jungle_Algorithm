import sys

# sys.stdin = open("input_py.txt")
input = sys.stdin.readline

N = int(input())

matrix = [[" "]*(2*N-1) for i in range(N)]

# print(matrix)


def starPrint(N, x, y):
    if N == 3:
        for i in range(3):
            for j in range(5):
                if (j + 1) % (3 - i) == 0:
                    matrix[x+i][y+j] = "*"

        return

    N //= 2
    starPrint(N, x, y+N)
    starPrint(N, x+N, y)
    starPrint(N, x+N, y+(2*N))


# matrix

starPrint(N, 0, 0)

for mat in matrix:
    print(*mat, sep='')
