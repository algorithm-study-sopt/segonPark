import sys

L = list()
for _ in range(9) :
    L.append(int(sys.stdin.readline()))
L.sort()
sumL = sum(L)

for i in range(9) :
    for j in range(i + 1, 9) :
        if sumL - L[i] - L[j] == 100 :
            for k in range(9) :
                if k == i or k == j : continue
                else : print(L[k])
            exit()

