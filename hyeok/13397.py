import sys

sys.stdin = open("input_py.txt")

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [int(x) for x in input().split()]

# print(f"N: {N}\nM:{M}\narr :{arr}")


def func(x):
    max_x = arr[0]
    min_x = arr[0]
    count = 1
    for i in range(1, N):
        max_x = max(max_x, arr[i])
        min_x = min(min_x, arr[i])
        if max_x - min_x > x:
            count += 1
            max_x = arr[i]
            min_x = arr[i]
    return count


left, right = 0, 10001


while left < right:
    mid = (left + right) // 2
    if func(mid) > M:
        left = mid + 1
    else:
        right = mid

print(left)
