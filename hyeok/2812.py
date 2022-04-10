import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())

number = input().strip()

print(f"N : {N}\nK : {K}\nnumber : {number}")


# count = 0

# start = 0
# answer = []
# 같은 숫자가 나오면 오답..... ㅜ ㅜ
# while True:
#     if count == (N - K):
#         break
#     tmp = max(number[start:N-K+count+1])
#     start = number.index(tmp) + 1
#     count += 1
#     answer.append(tmp)

# # print("answer : ", answer)

# # print("###")
# print(*answer, sep='')
