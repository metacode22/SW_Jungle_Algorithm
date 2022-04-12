import sys

sys.stdin = open("input_py.txt")

input = sys.stdin.readline

N, M = map(int, input().split())

lectures = list(map(int, input().split()))

print(lectures)


def func(x):
    count = 0
    sum_lecture = 0
    for i in range(N):
        if sum_lecture + lectures[i] > x:
            count += 1
            sum_lecture = 0
        sum_lecture += lectures[i]
    if sum_lecture:
        count += 1
    return count


for i in range(10):
    print(f"{i} {func(i)}")

# left = 1
# right = 10**10
left = max(lectures)
right = sum(lectures)+1
while left < right:
    mid = (left + right) // 2
    if func(mid) > M:
        left = mid + 1
    else:
        right = mid

print(left)
