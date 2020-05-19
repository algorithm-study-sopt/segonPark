import sys

N = int(input())
L = list(map(int, sys.stdin.readline().split()))

def isPrime(num) :
    if num == 1 : return False
    elif num == 2 : return True
    for i in range(2, num) :
        if num%i == 0 :
            return False
    return True

cnt = 0
for i in L :
    if isPrime(i) :
        cnt += 1
print(cnt)


