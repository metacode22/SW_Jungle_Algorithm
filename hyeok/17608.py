import sys

input = sys.stdin.readline

N = int(input())

sticks = [int(input()) for _ in range(N)]


# print(sticks)

standard = sticks.pop()
count = 1
for _ in range(N-1):
    comp = sticks.pop()
    if standard < comp:
        count += 1
        standard = comp

print(count)
