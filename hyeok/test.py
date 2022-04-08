import sys
all = []

while 1:
    t = input()
    if t == '0':
        break
    all.append(t)
# print(all)

for i in range(len(all)):
    all[i] = list(all[i].split())

# print(all)
case = []


def find(case):
    # case = [int(x) for x in case]
    if case.sort() in all_case:
        return False
    return True


def rotto(n, c):
    if n == 0:
        # print(all_case)
        if find(case):
            all_case.append(case)
            print(case)

    else:
        for a in range(1, int(c[0])+1):
            if c[a] not in case:
                case.append(c[a])
                rotto(n-1, c)
                case.pop()


for i in range(len(all)):
    c = all[i]  # 테스트 케이스
    all_case = []
    # print(c)
    rotto(6, c)  # (n,집합s)
    if i != (len(all)-1):
        print()
