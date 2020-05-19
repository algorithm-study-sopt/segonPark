import math
import sys


def isPrime(num) :
    L = num * [1]
    n = int(math.sqrt(num))
    for i in range(2, n+1) :
        if L[i] == 1 :
            for j in range(i+i, num, i) :
                L[j] = 0
    return L

L = isPrime(1000000)

while True :
    n = int(sys.stdin.readline())
    if n == 0 :
        break

    for i in range(3, n//2) :
        if L[i] and L[n-i] :
            print("{} = {} + {}".format(n, i, n-i))
            break

'''

import sys

def gold(n) :
    numbers = [1] * n

    for i in range(2, int(n**0.5)+1) :
        if numbers[i] == 1 :
            for j in range(i+i, n, i) :
                numbers[j] = 0
    return numbers

numbers=gold(1000000)
while True :
    n = int(sys.stdin.readline())
    if n==0 :
        break
    for i in range(3, n//2+1) :
        if numbers[i] and numbers[n-i] :
            print("{} = {} + {}".format(n,i,n-i))
            break
'''