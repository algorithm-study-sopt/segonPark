import sys


class Stack() :
    def __init__(self) :
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if len(self.stack) == 0 :
            return -1
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        if len(self.stack) == 0 :
            return 1
        else:
            return 0

    def top(self):
        if len(self.stack) != 0 : return self.stack[-1]
        else : return -1


stack_list = Stack()
N = int(sys.stdin.readline())
for i in range(N) :
    input_value = sys.stdin.readline().split()
    value = input_value[0]

    if value == "push" : stack_list.push(input_value[1])
    elif value == "pop" : print(stack_list.pop())
    elif value == "size" : print(stack_list.size())
    elif value == "empty" : print(stack_list.empty())
    elif value == "top" : print(stack_list.top())

