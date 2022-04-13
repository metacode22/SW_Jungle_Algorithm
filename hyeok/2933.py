import sys

sys.stdin = open("input_py.txt")
input = sys.stdin.readline

R, C = map(int, input().split())

matrix = [[0]*C for i in range(R)]
# input matrix

# N : 막대를 던진 횟수
# N = int(input())
# H : 막대를 던진 높이
# H = int(input())
# 아니 형님덜 저보고 이런 무지막지한 문제를 풀라고 하시는 겁니까 ????....

# bfs멀라영...
