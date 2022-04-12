import sys

sys.stdin = open("input_py.txt")

input = sys.stdin.readline

N, M = map(int, input().split())

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

A.extend(B)
A.sort()


print(*A)
