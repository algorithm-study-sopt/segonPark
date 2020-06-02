import heapq
import sys

N = int(sys.stdin.readline())
heap = list()
heapq.heapify(heap)

for i in range(N) :
    x = int(sys.stdin.readline())
    if x == 0 :
        if len(heap) == 0 :
            print(0)
        else :
            print(heapq.heappop(heap)[1]) #각 튜플의 인덱스가 1인 값을 가져옴
    else :
        heapq.heappush(heap, (-x, x))