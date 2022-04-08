import sys

input = sys.stdin.readline

N = int(input())

solution = sorted([int(x) for x in input().split()], key=abs)

minN = solution[0] + solution[1]

# 더 효율적으로 저장하는 방법이 없을까 ?
arr = [solution[0], solution[1]]
# num1 = solution[0]
# num2 = solution[1]

for i in range(1, N-1):
    if abs(minN) > abs(solution[i] + solution[i+1]):
        minN = solution[i] + solution[i+1]
        arr = [solution[i], solution[i+1]]
        # num1, num2 = solution[i], solution[i+1]
        # num1 = solution[i]
        # num2 = solution[i+1]


# print(arr)

# if num1 > num2:
#     print(num2, num1, sep=' ')
# else:
#     print(num1, num2, sep=' ')

# 이렇게 하면 indexError가 뜬ㄷㅏ 왜 ... ?
if arr[1] > arr[0]:
    print(arr[0], arr[1], sep=' ')
else:
    print(arr[1], arr[0], sep=' ')

# two pointer를 사용하여 푸는 방법도 있다.
# sort 쓰거
# left, right를 더해 음수면 left+1 양수면 right-1
