import sys

# sys.stdin = open("input_py.txt")
input = sys.stdin.readline

K, N = map(int, input().split())

lans = [int(input()) for i in range(K)]

# print(lans)


def func(x):
    count = 0
    # print(f"x: {x}")
    for lan in lans:
        # print(lan)
        count += lan//x
    return count


left, right = 0, max(lans)+1

while left < right:
    mid = (left + right) // 2
    # print(f" :: {func(mid)}")
    if func(mid) >= N:
        left = mid + 1
    else:
        right = mid

print(left-1)


# for i in range(10):
#     print(i, func(i+1))
