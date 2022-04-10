import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
cards = deque(range(1, N+1))

while cards:
    ans = cards.popleft()
    if len(cards) > 1:
        cards.append(cards.popleft())

print(ans)
