import sys

T = int(sys.stdin.readline())

# 1은 1 (1개)
# 2는 1+1, 2 (2개)
# 3은 1+1+1, 1+2, 2+1, 3 (4개)
# 0은 편의를 위해 넣음, 0은 0개

# 별개로 4는 7개, 5는 13개의 방법이 있다.
# 5까지 직접 구해본 결과 4부터 규칙이 존재함을 알 수 있다.
L = [0, 1, 2, 4]

for i in range(T) :
    N = int(sys.stdin.readline())
    # 4부터 (n-1)+(n-2)+(n-3)의 공식이 적용됨
    for j in range(4, N+1) :
        L.insert(j, L[j-1] + L[j-2] + L[j-3])
    print(L[N])
