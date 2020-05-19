import sys

N = int(sys.stdin.readline())

class Deque() :
    def __init__(self):
        self.deque = list()
    def push_front(self, num):
        self.deque.insert(0, num)
    def push_back(self, num):
        self.deque.append(num)

    def pop_front(self):
        if len(self.deque) == 0 : return -1
        else : return self.deque.pop(0)
    def pop_back(self):
        if len(self.deque) == 0: return -1
        else : return self.deque.pop()

    def size(self):
        return len(self.deque)
    def empty(self):
        if len(self.deque) == 0 : return 1
        else : return 0
    def front(self):
        if len(self.deque) == 0 : return -1
        else : return self.deque[0]
    def back(self):
        if len(self.deque) == 0 : return -1
        else : return self.deque[-1]

deque = Deque()
for i in range(N) :
    INPUT_VALUE = sys.stdin.readline().split()
    INPUT = INPUT_VALUE[0]

    if INPUT == "push_front" : deque.push_front(INPUT_VALUE[1])
    elif INPUT == "push_back" : deque.push_back(INPUT_VALUE[1])
    elif INPUT == "pop_front" : print(deque.pop_front())
    elif INPUT == "pop_back" : print(deque.pop_back())
    elif INPUT == "size" : print(deque.size())
    elif INPUT == "empty" : print(deque.empty())
    elif INPUT == "front" : print(deque.front())
    elif INPUT == "back" : print(deque.back())