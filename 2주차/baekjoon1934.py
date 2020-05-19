import sys

def GCD(A, B) :
    a, b = A, B
    while b != 0:
        a = a % b
        a, b = b, a
    return a

def LCM(A, B) :
    num = GCD(A, B)
    result = (A*B)//num
    return result

T = int(input())
for i in range(T) :
    A, B = map(int, sys.stdin.readline().split())
    print(LCM(A, B))