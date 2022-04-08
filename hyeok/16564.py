import sys

sys.stdin = open("./input_py.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())

X = [int(input()) for _ in range(N)]
# for _ in range(N):
#     X.append(int(input()))

# print(X)
X.sort()

result = 0


def level(leftV, rightV, arr):
    global result
    needL = 0
    midV = (leftV + rightV)//2
    if leftV > rightV:
        # result = max(result, midV)
        return
    for l in arr:
        if midV <= l:
            break
        else:
            needL += (midV - l)

    if needL > K:
        return level(leftV, midV-1, arr)
    else:
        # result = max(result, midV)
        result = midV
        return level(midV+1, rightV, arr)


level(X[0], X[N-1]+K, X)

print(result)
