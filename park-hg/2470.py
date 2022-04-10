import sys
sys.stdin = open('input.txt')
N = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
s.sort()

left, right = 0, len(s)-1
s1, s2 = s[left], s[right]
while left < right:
    if abs(s[left]+s[right]) < abs(s1+s2):
        s1, s2 = s[left], s[right]

    if s[left]+s[right] < 0:
        left += 1
    elif s[left]+s[right] > 0:
        right -= 1
    else:
        s1, s2 = s[left], s[right]
        break

print(s1, s2)