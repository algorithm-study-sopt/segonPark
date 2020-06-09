from itertools import permutations

n = int(input())
# permutation라이브러리를 사용
# permutation을 사용하게 되면 입력받은 수에 대한 모든 경우의 수를 tuple로 만들어 준다
arr = permutations(list(map(int, input().split())))

# 결과값으로 나올 변수 result를 0으로 초기화
result = 0

# permutation으로 입력받은 모든 수에 대한 경우의 수 tuple을 하나씩 i에 대입
for i in arr :
    # 튜플 내의 값들의 차의 합을 구하는 변수 sum
    sum = 0

    # range(n)을 하게되면 tuple index out of range 오류가 나온다.
    # [i], [j]식으로 색인화하게 되면 튜플 i+1, j+1 번째에 해당하는 값을 가져오려 하기 때문에 오류가 난다.
    # for문을 통해 각 tuple별 sum 계산
    for j in range(n-1) :
        process = abs(i[j] - i[j+1])
        sum += process

    # 비교 대상인 result와 sum을 max함수로 비교하여 큰 값을 result에 저장하여 모든 튜플을 수행할 때까지 반복
    result = max(result, sum)
print(result)

