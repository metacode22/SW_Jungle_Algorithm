import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

class FixedStack:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    # is_empty
    def empty(self):
        if self.ptr <= 0:
            return 1
        else:
            return 0

    def is_full(self):
        return self.ptr >= self.capacity

    def push(self, value):
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self):
        if self.empty():
            return -1
        else:
            self.ptr -= 1
            return  self.stk[self.ptr]

    # __len__
    def size(self):
        return self.ptr

    # peek
    def top(self):
        if self.empty():
            return -1
        else:
            return self.stk[self.ptr - 1]

stack = FixedStack(10000)

n = int(input())
for i in range(n):
    cmd = list(map(str, input().split()))
    if cmd[0] == 'push':
        stack.push(int(cmd[1]))

    if cmd[0] == 'pop':
        print(stack.pop())

    if cmd[0] == 'size':
        print(stack.size())

    if cmd[0] == 'empty':
        print(stack.empty())

    if cmd[0] == 'top':
        print(stack.top())
