import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n, c = map(int, input().split())
x = []
for _ in range(n):
    x.append(int(input()))
x.sort()

def count(len):
    cnt = 1
    point = x[0]
    for i in range(1, n):
        if x[i] - point >= len:
            cnt += 1
            point = x[i]

    return cnt

lt = 1
rt = x[n - 1] - x[0]
res = 0
while lt <= rt:
    mid = (lt+rt) // 2
    if count(mid) >= c:
        lt = mid + 1
        res = mid
    else:
        rt = mid - 1

print(res)