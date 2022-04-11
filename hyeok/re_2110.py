import sys

sys.stdin = open("input_py.txt")
input = sys.stdin.readline

N, C = map(int, input().split())

xs = [int(input()) for _ in range(N)]

xs.sort()

left = -1
right = 10**9 + 1


def func(x):
    count = 1
    start = xs[0]
    for i in range(1, len(xs)):
        if xs[i] - start >= x:
            count += 1
            start = xs[i]
    return count


# func 증가면 < <=
# func 감소면 > >=
for i in range(10):
    print(i, func(i))
while left < right:
    mid = (left + right) // 2
    # 등호가 같으면 움직이냐
    if func(mid) >= C:
        left = mid + 1
    else:
        right = mid


print(left - 1)
