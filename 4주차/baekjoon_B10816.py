import sys

N = int(sys.stdin.readline())
L1 = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
L2 = list(map(int, sys.stdin.readline().split()))

d = dict() #dictionary형 변수 d 선언

for i in L1 : #L1에 있는 값을 i에 차례대로 대입
    key = d.keys() #d의 key 값을 key 변수에 할당
    if i in key : #i 값이 key 변수 안에 있다면 d의 i번째 값에 1만큼 더함(갯수)
        d[i] += 1
    else : #그렇지 않으면 1 대입(key에 해당하는 값이 하나라도 있으니까)
        d[i] = 1

for j in L2 : #L2에 있는 값들이 key 값 중 일치하는 것이 있는지 확인
    if j in key :
        print(d[j], end = " ")
    else :
        print(0, end = " ")







# for j in L2:
#     cnt = 0
#     for k in L1:
#         if j == k:
#             cnt += 1
#
#     print(cnt)


