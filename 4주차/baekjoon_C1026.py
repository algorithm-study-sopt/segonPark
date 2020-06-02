import sys


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

# A 리스트의 가장 작은수 * B 리스트의 가장 큰수를 곱하고 전체 sum을 했을 때 최솟값이 나온다
# 먼저 min(A)로 A 리스트의 최소값을 구하고, A.index로 최소값의 index를 구하고 이를 pop한다.
# B도 마찬가지로 최댓값을 구하고 가장 먼저 pop한 A,B의 값을 곱한 뒤 result에 더해준다.
# N번만큼 돌면서 pop을 하고 곱하기 때문에 for문을 모두 돈 뒤 각 리스트에는 값이 없다.
result = 0
for i in range(N) :
    result += A.pop(A.index(min(A)))*B.pop(B.index(max(B)))
print(result)