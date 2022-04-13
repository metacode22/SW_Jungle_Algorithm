import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, list(input().rstrip())))
stack = []

# 앞에서부터 비교해가며 지우는 것이 좋다.
# 7 2
# 6 1 2 4 3 2 1 이라고 했을 때 뒤의 2 1 을 지우는 것이 아니라 (61243)
# 앞의 1 2 를 지우는 것이 더 큰 수를 만든다. (64321)
# 처음엔 그냥 넣고
# 뒤에 들어오는 수가 스택의 탑보다 작다면 일단 넣는다. 뒤에 자기보다 작은 수들이 올 수 있으니까
# 만약 스택의 탑이 들어오는 수보다 작다면 지우는 것이 유리하다. 들어오는 수가 더 크니까 앞의 자리로 갈수록 유리해지기 때문이다.
for i in a:
    while stack and stack[-1] < i and k:
        stack.pop()
        k -= 1
    stack.append(i)
    
while k:
    stack.pop()
    k -=1

stack_str = list(map(str, stack))   # 덜 지웠을 경우, 덜 지운 만큼 뒤에서부터 지워줘야 한다. 앞에는 큰 수들이 모여 있으므로 뒤의 수를 지우는 것이 맞다.
print(''.join(stack_str))