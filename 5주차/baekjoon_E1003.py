import sys

T = int(sys.stdin.readline())
c0 = [1, 0]
c1 = [0, 1]

for i in range(2, 41) :
    c0.append(c0[i-1] + c0[i-2])
    c1.append(c1[i-1] + c1[i-2])

for j in range(T) :
    n = int(sys.stdin.readline())
    print(c0[n], c1[n])
