import sys

sys.stdin = open("input_py.txt")

input = sys.stdin.readline

N = int(input())

circles = []

for i in range(N):
    c, r = list(map(int, input().split()))
    # 1 : Left // -1 : Right
    circles.append((1, c-r))
    circles.append((-1, c+r))

#     circles.append(("L", c-r))
#     circles.append(("R", c+r))

circles.sort(key=lambda x: (x[1], x[0]))
# circles.sort(key=lambda x: (-x[1], x[0]), reverse=True)

print(circles)

stack = []
area = 1

for curr in circles:
    # 왼쪽 끝인 경우
    if curr[0] == 1:
        stack.append(curr)
        continue
    # 오른쪽 끝인 경우
    cum_width = 0
    while stack:
        prev = stack.pop()
        # 본인 내부에 원이 있었으면, 해당 원의 너비를 누적 // 0 : 넓이
        if prev[0] == 0:
            cum_width += prev[1]
        # Right(1)이 나올때마다 Left(-1)을 pop해주므로 처음 만난 L이 본인과 동일한 원에서 나온 값임
        elif prev[0] == 1:
            # 원의 넓이를 계산
            width = curr[1] - prev[1]
            # 내부에 잇는 원들의 너비 합산이 본인의 너비와 일치하는지 확인
            if width == cum_width:
                area += 2
            else:
                area += 1
            # 다른 원에 포함될 수 있으므로 추가
            stack.append((0, width))
            break

print(area)
