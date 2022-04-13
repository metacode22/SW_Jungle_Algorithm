# 다시풀기
import sys

# sys.stdin = open("input_py.txt")
input = sys.stdin.readline

N = int(input())
k = int(input())


def func(x):
    count = 0
    for i in range(1, N+1):
        count += min(x//i, N)
    return count


def binary():
    left = 0
    right = k+1

    # func 증가면 < <=
    # func 감소면 > >=
    while left < right:
        mid = (left + right) // 2
        # 등호가 같으면 움직인다.
        if func(mid) < k:
            left = mid + 1
        else:
            right = mid
    return left


print(binary())
