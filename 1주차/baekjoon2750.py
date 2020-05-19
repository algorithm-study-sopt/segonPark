N = int(input())
M = []

for i in range(N) :
    M.append(int(input()))

M.sort()
for i in range(len(M)) :
    print(M[i])
