import sys

# 좌표의 개수 N을 받음
N = int(sys.stdin.readline())

# 좌표 X, Y를 받을 list 생성
L = list()

# N개의 좌표를 만들어 처음 만들어놓은 list L에 list형식으로 append한다.
# [[1,2], [1,5]]와 같은 형식으로 저장됨.
for i in range(N) :
    X, Y = map(int, sys.stdin.readline().split())
    L.append([X, Y])

# sort함수로 list L 정렬(오름차순)
# x좌표가 같은 경우 y좌표 기준으로 정렬해서 나타남.
L.sort()

# 2중 for문을 쓰지 않고 원소의 값 추출
for i in range(N) :
    print(L[i][0], L[i][1])