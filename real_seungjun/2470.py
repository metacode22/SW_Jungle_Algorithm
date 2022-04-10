import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

lt = 0
rt = n - 1
min = 2147000000
while lt < rt:
    tot = a[lt] + a[rt]

    if abs(tot) < min:
        res_lt = lt
        res_rt = rt
        min = abs(tot)
        if abs(tot) == 0:
            break

    if tot < 0:
        lt += 1
    elif tot > 0:
        rt -= 1

print(a[res_lt], a[res_rt])
