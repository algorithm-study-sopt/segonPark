import sys

N = int(input())
M = []

for i in range(N) :
    M.append(int(sys.stdin.readline()))

M = sorted(M)
for i in range(len(M)) :
    print(M[i])
