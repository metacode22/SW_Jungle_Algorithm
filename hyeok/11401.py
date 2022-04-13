import sys

sys.stdin = open("input_py.txt")
input = sys.stdin.readline

N, K = map(int, input().split())
# binomial coefficient


def binomial(para, meter):
    answer = factorial(para) / (factorial(meter) * factorial(para-meter))

    return answer


def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1) % 1000000007


print(int(binomial(N, K)))
