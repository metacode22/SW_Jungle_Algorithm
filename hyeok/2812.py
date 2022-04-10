# T _ T
import sys

# sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())

number = list(map(int, input().strip()))

result = []
delNum = K

for i in range(N):
    while delNum > 0 and result:
        if result[-1] < number[i]:
            result.pop()
            delNum -= 1
        else:
            break
    result.append(number[i])

for i in range(N-K):
    print(result[i], end='')

# count = 0

# start = 0
# answer = []

# while count < N-K:
#     tmp = max(number[start:K+count+1])
#     start += number[start:K+count+1].index(tmp) + 1
#     count += 1
#     answer.append(tmp)

# print(*answer)
# # print(''.join(map(str, answer)))
