import sys

N = int(sys.stdin.readline())

class QUEUE() :
    def __init__(self):
        self.queue = list()

    def push(self, x) :
        self.queue.append(x)

    def pop(self):
        if len(self.queue) == 0 : return -1
        else : return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def empty(self):
        if len(self.queue) == 0 : return 1
        else : return 0

    def front(self):
        if len(self.queue) == 0: return -1
        else : return self.queue[0]

    def back(self):
        if len(self.queue) == 0 : return -1
        else : return self.queue[-1]

queue = QUEUE()

for i in range(N) :
    INPUT_VALUE = sys.stdin.readline().split()
    INPUT = INPUT_VALUE[0]

    if INPUT == "push" : queue.push(INPUT_VALUE[1])
    elif INPUT == "pop" : print(queue.pop())
    elif INPUT == "size" : print(queue.size())
    elif INPUT == "empty" : print(queue.empty())
    elif INPUT == "front" : print(queue.front())
    elif INPUT == "back" : print(queue.back())

