# 다시풀기
import sys

sys.stdin = open("input_py.txt")
input = sys.stdin.readline

N = int(input())
k = int(input())

left = 0
right = k
answer = 0


def func(x):
    count = 0
    for i in range(1, N+1):
        count += min(x//i, N)
    return count


while left < right:
    mid = (left + right) // 2
    if func(mid) < k:
        left = mid + 1
    else:
        right = mid
print(right)
