import sys

# https://hooongs.tistory.com/201?category=823477 블로그의 나라야나 판디타가 고안한 알고리즘 방법
N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
k = -1 #아래의 조건에 만족하지 않는 한 내림차순임

# k의 최댓값
# i+1로 인해 마지막 값이 N-1까지 도달함
for i in range(N - 1):
    if L[i] < L[i + 1]:
        k = i

# 내림차순의 경우
if k == -1:
    print(-1)

# m의 최댓값
else:
    for j in range(k + 1, N):
        if L[k] < L[j]:
            m = j

    # k와 m 값 바꾸기
    L[k], L[m] = L[m], L[k]
    # k 이후 정렬
    temp = L[k + 1:]
    temp.sort()
    result = L[:k + 1] + temp

    for num in result:
        print(num, end=' ')
    # print()



    # # 내 코드
    #
    # N = int(sys.stdin.readline())
    # L = list(map(int, sys.stdin.readline().split()))
    # last = -1
    #
    # for i in range(N - 1):
    #     if L[i] < L[i + 1]:
    #         last = i
    #
    # if last == -1:
    #     print(-1)
    #
    # else:
    #     for j in range(last + 1, N):
    #         if L[last] < L[j]:
    #             M = j
    #
    #     L[last], L[M] = L[M], L[last]
    #
    #     LL = L[M + 1:]
    #     LL.sort()
    #     result = L[:M + 1] + LL
    #
    #     for k in result:
    #         print(k, end=' ')
    #     print()