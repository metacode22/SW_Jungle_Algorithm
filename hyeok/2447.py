import sys

sys.stdin = open("input_py.txt")

input = sys.stdin.readline

N = int(input())

starMatrix = [[" "]*N for i in range(N)]


def sol(N, x, y):
    if N == 3:
        for i in range(N):
            for j in range(N):
                if i == 1 and j == 1:
                    continue
                starMatrix[x+i][y+j] = "*"
        # starMatrix[x+1][y+1] = ""

        return
        # starMatrix[x+1][y+1] = ""

    N //= 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            sol(N, x+(N*i), y+(N*j))


sol(N, 0, 0)

# print(starMatrix)

for star in starMatrix:
    print(*star, sep='')
