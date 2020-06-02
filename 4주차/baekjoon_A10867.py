import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
LL = list(set(L))
LL.sort()
for i in range(len(LL)) :
    print(LL[i], end = " ")