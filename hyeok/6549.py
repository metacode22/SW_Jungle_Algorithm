# 다시 풀기
import sys
from collections import deque
input = sys.stdin.readline

while True:
    rec = [int(x) for x in input().split()]
    # print(rec)
    n = rec.pop(0)

    if n == 0:
        break
    # stack = deque()
    stack = deque()
    answer = 0
    # print("n:", n)
    # print("rec : ", rec)

    for i in range(n):
        # rec[stack[-1]] : 이전값 // rec[i]: 현재값
        while len(stack) != 0 and rec[stack[-1]] > rec[i]:
            # print("stack[-1] : ", stack[-1])
            # print("i", i)
            tmp = stack.pop()

            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1
            answer = max(answer, width * rec[tmp])
        stack.append(i)
    # 스택 남아잇는 거 처리 .....와,,, 천재다
    while len(stack) != 0:
        tmp = stack.pop()

        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] - 1
        answer = max(answer, width * rec[tmp])

    print(answer)
