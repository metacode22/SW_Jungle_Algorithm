import sys


input = sys.stdin.readline

T = int(input())

VPSs = [input().strip() for i in range(T)]

for VPS in VPSs:
    stack = []
    flag = True
    for i in range(len(VPS)):
        if VPS[i] == '(':
            stack.append("1")
        else:
            if len(stack) <= 0:
                # print("NO")
                flag = False
                break
            stack.pop()
    if len(stack) == 0 and flag == True:
        print("YES")
        # print(len(stack))
    else:
        print("NO")
        # print(len(stack))

# print(VPSs)
