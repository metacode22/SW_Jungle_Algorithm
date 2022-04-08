# 다시 풀긔?
import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())


def remain(num1, num2):
    if num2 == 1:
        return num1 % C
    else:
        tmp = remain(num1, num2//2)
        if num2 % 2 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * num1) % C


print(remain(A, B))
# 메모리 초과
# dp = [0]*(B+1)

# dp[1] = A % C
# for i in range(2, B+1):
#     if i % 2 == 0:
#         dp[i] = (dp[i//2] * dp[i//2]) % C
#     else:
#         dp[i] = (dp[i//2] * dp[i//2] * A) % C

# print(dp[B])

# # print(A % C)
