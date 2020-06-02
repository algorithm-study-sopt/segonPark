import sys

N = int(sys.stdin.readline())
L = [0 for _ in range(N+1)]

for i in range(1, N + 1) :
    if i == 1 :
        L[i] = 0
        continue
    L[i] = L[i-1] + 1
    if i % 2== 0 and L[i] > L[i//2] + 1 :
        L[i] = L[i//2] + 1
    if i % 3 == 0 and L[i] > L[i//3] + 1 :
        L[i] = L[i//3] + 1
print(L[i])