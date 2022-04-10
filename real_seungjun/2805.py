import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
line = list(map(int, input().split()))
longest = max(line)

def count(len):
    rest = 0

    for i in line:
        if len >= i:
            continue
        else:
            rest += i - len

    return rest

lt = 1
rt = longest
res = 0
while lt <= rt:
    mid = (lt+rt) // 2

    if count(mid) >= m:
        lt = mid + 1
        res = mid

    else:
        rt = mid - 1

print(res)