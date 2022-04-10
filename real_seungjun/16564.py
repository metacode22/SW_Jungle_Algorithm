import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
x = []
for _ in range(n):
    x.append(int(input()))

def check(level):
    tot = 0
    for i in x:
        if i < level:
            tot += level - i
    if tot > k :
        return False
    elif tot <= k :
        return True

lt = min(x)
rt = max(x) + k
while lt <= rt:
    mid = (lt+rt) // 2

    if check(mid):
        lt = mid + 1
        res = mid
    else:
        rt = mid - 1

print(res)
