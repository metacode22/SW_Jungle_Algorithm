import sys

sys.stdin = open("input_py.txt")
input = sys.stdin.readline

N, k = map(int, input().split())


def searchLen(num):  # 1 ~ num까지의 자릿수 구하는 함수
    length = len(str(num))
    res = 0

    for i in range(1, length):
        res += i * ((10**i) - (10**(i-1)))
        # res += i * (pow(10, i) - pow(10, i - 1))

    # res += length * (num - pow(10, length - 1) + 1)

    res += length * (num - (10 ** (length-1)) + 1)

    return res


left, right = 1, N

if searchLen(N) < k:
    print(-1)
    sys.exit()

while left < right:
    mid = (left + right) // 2
    if searchLen(mid) < k:
        left = mid+1
    else:
        right = mid
        # ans = mid


# print(searchLen(right))
idx = searchLen(right) - k + 1
right = str(right)
print(int(right[-idx]))
