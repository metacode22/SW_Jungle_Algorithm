import sys

sys.stdin = open('input.txt')
N = int(sys.stdin.readline())
points = []
for _ in range(N):
    x, r = map(int, sys.stdin.readline().split())
    points.append([0, x-r])
    points.append([1, x+r])

points.sort(key=lambda x: (x[1], -x[0]))

stack = []
area = 1
for pos, x in points:
    if pos == 0:
        stack.append([pos, x])
    else:
        sub_sum = 0
        while stack:
            top = stack.pop()
            if top[0] == 2:
                sub_sum += top[1]
            else:
                if x - top[1] == sub_sum:
                    area += 2
                else:
                    area += 1
                stack.append([2, x-top[1]])
                break

print(area)