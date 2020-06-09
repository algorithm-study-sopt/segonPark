import sys
from itertools import combinations_with_replacement

# 방법1 generator 사용
N, M = map(int, sys.stdin.readline().split())
L = [i for i in range(1, N+1)]

# 중복조합
def recursive_combination(arr, r) :
    for i in range(len(arr)) :
        if r == 1 :
            yield [arr[i]]
        else :
            # r == 1일때를 이미 뽑았기 때문에 r-1개를 마저 뽑는다
            # 1 1 1, 1 1 2 이런식으로 한번 뽑은 수를 다시 쓰므로 i+1이 아닌 i번 부터 다시 시작
            for j in recursive_combination(arr[i:], r-1) :
                yield [arr[i]] + j


for k in recursive_combination(L, M) :
    for l in k :
        print(l, end = ' ')
    print()


'''
# 방법 2 combinations_with_replacement 라이브러리 사용

# combinations_with_replacement는 중복조합으로 (1, 2), (2, 1)을 똑같은 것으로 간주하여 (1, 2)만 출력한다.
# combinations_with_replacement(반복할 리스트, 뽑을 숫자 수)를 입력하면 된다.
for segon in combinations_with_replacement(L, M) :
    for j in segon :
        print(j, end = " ")
    print() # for i in segon문 안에 쓰면 한 글자 단위로 개행이 됨
'''