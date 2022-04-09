import sys

sys.stdin = open("input_py.txt", "r")

input = sys.stdin.readline

N = int(input())

towers = [int(x) for x in input().split()]

stack = []
answer = []
for i in range(N):
    while stack:
        if stack[-1][1] > towers[i]:  # 수신 가능한 상황
            answer.append(stack[-1][0] + 1)
            # print(stack[-1][0]+1, end=' ')
            break
        else:
            stack.pop()
    if not stack:  # 스택이 비면 레이저를 수신할 탑이 없다.
        answer.append(0)
        # print(0, end=' ')
    stack.append([i, towers[i]])  # 인덱스, 값
# print()
print(" ".join(map(str, answer)))
# print(*answer)
# stack = [0, towers.popleft()]
# answer = [0]

# flag = False
# time over ...??
# for i in range(N-1):
#     flag = False
#     height = towers.popleft()
#     lengthS = len(stack)
#     for j in range(lengthS-1, 0, -1):
#         if stack[j] > height:
#             answer.append(j)
#             stack.append(height)
#             flag = True
#             break
#     if flag == False:
#         stack.append(height)
#         answer.append(0)
#         # flag 줘야하나? 못찾은 경우, 즉 0 일 경우 어/케행

# print(*answer)
# print()
# print(f"stack : {stack}")
