import sys

sys.stdin = open("input_py.txt")

input = sys.stdin.readline

N = int(input())

matrix = [[int(x) for x in input().split()]for i in range(N)]

# print(matrix)

minus = 0
zero = 0
plus = 0


def sol(N, x, y):
    global minus, zero, plus
    standard = matrix[x][y]
    for i in range(N):
        for j in range(N):
            if matrix[x+i][y+j] != standard:
                for k in range(3):
                    for l in range(3):
                        sol(N//3, x+(N//3*k), y+(N//3*l))
                return
    if standard == -1:
        minus += 1
    elif standard == 0:
        zero += 1
    else:
        plus += 1
    return


sol(N, 0, 0)

print(minus)
print(zero)
print(plus)
