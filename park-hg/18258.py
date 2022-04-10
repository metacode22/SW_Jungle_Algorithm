import sys
sys.stdin = open('input.txt')

class LinkedList():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Queue():
    def __init__(self):
        self.front = self.back = None
        self.size = 0

    def push(self, val):
        if self.size == 0:
            self.front = self.back = LinkedList(val)
            self.size = 1
            return
        
        self.back.next = LinkedList(val)
        self.back = self.back.next
        self.size += 1

    def pop(self):
        if self.size == 0:
            return -1

        if self.size == 1:
            val = self.front.val
            self.front = self.back = None
            self.size = 0
            return val
        
        val = self.front.val
        self.front = self.front.next
        self.size -= 1
        return val

    def empty(self):
        return 1 if self.size==0 else 0


que = Queue()

N = int(sys.stdin.readline())
for _ in range(N):
    query = sys.stdin.readline().rstrip().split()
    if query[0] == "push":
        que.push(int(query[1]))

    elif query[0] == "pop":
        print(que.pop())

    elif query[0] == "size":
        print(que.size)

    elif query[0] == "empty":
        print(que.empty())

    elif query[0] == "front":
        if que.front is not None:
            print(que.front.val)
        else:
            print(-1)

    elif query[0] == "back":
        if que.back is not None:
            print(que.back.val)
        else:
            print(-1)